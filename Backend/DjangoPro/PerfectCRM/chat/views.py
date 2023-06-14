from django.shortcuts import render

# Create your views here.
import openai

# API密钥
OPENAI_SECRET_KEY = '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'
# 设置API密钥
openai.api_key = OPENAI_SECRET_KEY

# 设置问题
question = '使用python实现快速排序'

response = openai.Completion.create(
    model='text-davinci-003',
    prompt=question,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# ChatGPT的回复
answer = response.choices[0].text.strip()

print("问：", question)
print("答：", answer)