#-*- encoding: utf-8 -*-
import speech_recognition as sr

# 创建一个Recognizer对象
r = sr.Recognizer()

# 读取录音文件
audio_file = sr.AudioFile('/Users/apple/Pypro/Backend/DjangoPro/DRFPro/思琪面试录音.wav')
# 使用Recognizer对象将音频文件转换为文本
with audio_file as source:
    audio = r.record(source)  # 获取音频数据
    text = r.recognize_google(audio, language='zh-CN')  # 将音频数据转化为中文文本

# 打印转换后的文本
print(text)
