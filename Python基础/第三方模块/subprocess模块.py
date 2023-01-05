#-*- encoding: utf-8 -*-
import subprocess

res1 = subprocess.Popen(
    "dir | findstr html*",  # 使用管道符号运行命令
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

result = res1.stdout.read()
result = str(result, encoding="gbk")
print(result)