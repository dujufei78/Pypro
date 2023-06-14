# -*- encoding: utf-8 -*-

import json
import time

import requests
import urllib3


def re_chat(texta, question):
    url = 'https://api.openai.com/v1/completions'
    # url = 'http://cgt.jahwaec.com'
    header = {'Content-type': 'application/json',
              'Authorization': "Bearer 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"}
    data = {
        'model': 'text-davinci-003',
        'prompt': texta + 'Human:' + question,
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
    res = json.loads(response.content)['choices'][0]['text']
    print(res)
    return res


if __name__ == '__main__':
    res = re_chat('', '你知道成都么')
    time.sleep(8)
    re_chat(res, '你知道那里有什么好玩的么')
