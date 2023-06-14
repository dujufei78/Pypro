from django.test import TestCase

# Create your tests here.
import json

import requests


def chat_url(prompt):
    '''
    调用接口的方式获取chatgpt的答案
    :return:
    '''
    try:
        sectet_key = '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'
        # sectet_key = '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'
        url = 'https://api.openai.com/v1/completions'
        # url = 'http://cgt.jahwaec.com'
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
        rrr = json.loads(response.content)
        print(rrr)

        res = json.loads(response.content)['choices'][0]['text'].strip()
        print(res)
        return res
    except Exception as e:
        print(str(e))
        return str(e)


if __name__ == '__main__':
    chat_url('以“建设工程领域相关法律风险研究”为主题，写一篇500字的议论文')

