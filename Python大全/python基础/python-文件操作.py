#-*- encoding: utf-8 -*-
# seek和tell光标

f = open('libai.ini', encoding='utf-8')
data = f.read()
data1 = f.read()
print(data)
print('===')
print(data1)  # 这样打印的data1是空值，如何让data1打印第1行呢？ seek

print(f.tell())
f.seek(0)  # 将光标移动到文件初始位置
print(f.readline().strip())
f.close()  # open需要手动关闭，with open自动关闭

# 模拟进度条
import sys, time

for i in range(40):
    sys.stdout.write('#')
    sys.stdout.flush()  # 可以用在网络程序中多线程程序，多个线程后台运行，同时要能在屏幕上实时看到输出信息。
    time.sleep(0.1)

# 读写方式说明
# r: 用于读，指针会放到文首
# w:用于写入，文件存在就覆盖，没有则创建
# a:追加，文件不存在，则创建写入
# rb:已二进制打开文件，用于只读
# r+  :打开一个文件，用于读写.文件指针会在开头
# w+  :打开一个文件，用于读写.文件存在则覆盖，文件不存在则创建写入
# a+  :打开一个文件，用于读写.文件存在指针放到末尾，不存在则创建读写
# rb+ :打开一个文件，用于读写.以二进制打开文件读写，指针放到开头