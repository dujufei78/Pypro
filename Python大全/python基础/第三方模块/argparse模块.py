#-*- encoding: utf-8 -*-
# 1.argparse功能
# 是python的命令解析的第三方包，可以直接让我们在命令行向程序里传参和修改参数

# 2.例子

# import argparse
# parser = argparse.ArgumentParser() # 创建ArgumentParser对象
# parser.add_argument('number', help='请输入数字', type=int) # 添加必选参数
# parser.add_argument('str', help="请输入字符串", type=str) # 添加必选参数
# args = parser.parse_args() # 解析参数
# print(args.number + 10)
# print(args.str)

# 然后打开命令行运行 python argparse_test.py 10 du
# 输出：20 du   # 按照添加参数的顺序输入参数，要不然会报错
# 输入：python argparse_test.py -h 会输出所有的提示信息

# 3.可选参数（与默认值default）、必选参数

# import argparse
# parser = argparse.ArgumentParser() # 创建ArgumentParser对象
# subparser = parser.add_subparsers(title = 'subcommands', description='')
# parser.add_argument('--number', help='请输入数字', type=int) # 添加可选参数
# parser.add_argument('--str', help="请输入字符串", type=str, default= 'hello', required=True) # 添加可选参数
# # required=true时变为了必选参数
# # default='xxxx' 可选参数，不输入参数时会输出默认值
# args = parser.parse_args() # 解析参数
# print(args)
# print(args.number + 10)
# print(args.str)

# 打开命令行运行python argparse_test.py  --number=3 --str='du'
# 可选参数命令行输入时得用  --xxx=ooo 格式
# 输出：Namespace(number=3, str="'du'")

# 4. action

# import argparse
# parser = argparse.ArgumentParser() # 创建ArgumentParser对象
# parser.add_argument('--xxx', help='请输入', action='store_true')
# args = parser.parse_args() # 解析参数
# print(args.xxx)

# action=‘store_true’，在运行时该变量不需要传入参数（且不能传入参数），只要写明该变量他就自动就变为True，如果不写该变量则为False
# 打开命令行运行 python argparse_test.py --xxx  输出：True