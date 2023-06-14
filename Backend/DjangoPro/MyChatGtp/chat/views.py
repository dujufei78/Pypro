# -*- coding: utf-8 -*-
import json
import redis
import openai
import requests
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from MyChatGtp.settings import host, port, sectet_key, mychat_url


def get_answer(prompt):
    text = ""  # 设置一个字符串变量
    turns = []  # 设置一个列表变量，turn指对话时的话轮
    while True:  # 能够连续提问
        question = input()
        if len(question.strip()) == 0:  # 如果输入为空，提醒输入问题
            print("please input your question")
        elif question == "quit":  # 如果输入为"quit"，程序终止
            print("\nAI: See You Next Time!")
            break
        else:
            prompt = text + "\nHuman: " + question
            result = chat(prompt)
            while result == "broken":  # 问不出结果会自动反复提交上一个问题，直到有结果为止。
                print("please wait...")
                result = chat(prompt)  # 重复提交问题
            else:
                turns += [question] + [result]  # 只有这样迭代才能连续提问理解上下文
                # print(result)
            if len(turns) <= 10:  # 为了防止超过字数限制程序会爆掉，所以提交的话轮语境为10次。
                text = " ".join(turns)
            else:
                text = " ".join(turns[-10:])


def chat_url(prompt):
    '''
    调用接口的方式获取chatgpt的答案
    :return:
    '''
    try:
        url = mychat_url
        header = {'Content-type': 'application/json',
                  'Authorization': "Bearer " + sectet_key}
        data = {
            'model': 'text-davinci-003',
            'prompt': prompt,
            # 'prompt': question,
            'temperature': 0.9,
            'max_tokens': 2500,
            'top_p': 1,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.6,
            'stop': ["Human:", "AI:"],
        }
        # urllib3.disable_warnings()
        response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
        res = json.loads(response.content)['choices'][0]['text'].strip()
        return res
    except Exception as e:
        return "openai连接异常，请重新输入"


def con_redis():
    '''
    连接redis
    '''
    try:
        conn = redis.Redis(host=host, port=port)
        return conn
    except Exception as e:
        print(e)
        return HttpResponse({'message': str(e)})


def chat(prompt):  # 定义一个函数，以便后面反复调用
    '''
    Getting answer usering openai.
    :param prompt:
    :return:
    '''
    try:
        OPENAI_SECRET_KEY = sectet_key
        # 设置API密钥
        openai.api_key = OPENAI_SECRET_KEY
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        answer = response["choices"][0]["text"].strip()
        return answer
    except Exception as exc:
        # print(exc)  #如果需要打印出故障原因可以使用本行代码，如果想增强美感，就屏蔽它。
        return "openai连接异常，请重新输入"


def chat_final(request):
    # 连接redis
    con = con_redis()
    con.expire('chat_list', 5000)  # 设置过期时间

    # 处理特殊情况
    mytext = request.POST.get('mytext')
    if mytext == None:  # 如果输入为空，提醒输入问题
        return render(request, 'mychat/final_index.html')
    elif mytext == "quit":  # 如果输入为"quit"，清除chat记忆
        con.delete('chat_list')
        return render(request, 'mychat/final_index.html')

    # 往redis写入数据-问题
    con.lpush('chat_list', 'Me: %s' % mytext)

    # 联系上下文，拼接上下文答案+问题
    chat_all_message = con.lrange('chat_list', 0, 10)
    chat_all_message.reverse()
    chat_all_message = [i.decode('utf-8') for i in chat_all_message]
    chat_all_message = ['' + '\n' + j[4:] for j in chat_all_message]
    chat_all_message = ''.join(chat_all_message)
    print('=====all=====')
    print(chat_all_message)

    # 调用openai接口，获取答案
    mytext = chat_all_message + '\n' + mytext

    # 使用python-openai模块实现聊天功能
    # answer = chat(mytext)

    # 使用requests方法-调用接口实现功能
    answer = chat_url(mytext)

    # 往redis写入数据-答案
    con.lpush('chat_list', 'Ai: %s' % answer)
    chat_list = con.lrange('chat_list', 0, 10)
    print(chat_list, type(chat_list))
    # 处理redis里的数据作展示
    l = []
    for i in chat_list:
        l.append(i.decode('utf-8'))
    l.reverse()
    # 联系上下文调用openai,之前的内容+问题，传参

    return render(request, 'mychat/final_index.html', {'chat_list': l, 'answer': answer})

def index(request):
    return render(request, 'mychat/index.html')