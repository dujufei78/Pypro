# -*- encoding: utf-8 -*-

import json

import requests
import urllib3


def chat(question):
    try:
        url = 'https://api.openai.com/v1/completions'
        # url = 'http://cgt.jahwaec.com'
        header = {'Content-type': 'application/json',
                  'Authorization': "Bearer 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"}
        data = {
            'model': 'text-davinci-003',
            'prompt': 'Human:' + question,
            # 'prompt': question,
            'temperature': 0.9,
            'max_tokens': 2500,
            'top_p': 1,
            'frequency_penalty': 0.0,
            'presence_penalty': 0.6,
            'stop': ["Human:", "AI:"],
        }
        urllib3.disable_warnings()
        response = requests.post(url=url, data=json.dumps(data), headers=header, verify=False)
        res = json.loads(response.content)
        answer = res["choices"][0]["text"].strip()
        return answer
    except Exception as e:
        print(e)
        return 'Broken'


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
