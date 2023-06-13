# -*- encoding: utf-8 -*-
'''创建一个堆栈'''


# class Stack():
#     def __init__(self):
#         self.items = []  # 初始化列表
#
#     def push(self, item):
#         self.items.append(item)  # 入栈操作，使用列表的插入操作
#
#     def pop(self):
#         return self.items.pop()  # 出栈操作，使用列表的删除操作完成
#
#     def is_empty(self):
#         return self.items == []  # 判断堆栈是否为空
#
#     def peek(self):
#         if not self.is_empty():  # 查看栈顶元素
#             return self.items[-1]
#
#     def get_stack(self):  # 获得整个堆栈
#         return self.items


# myStack = Stack()  # 创建一个堆栈
# myStack.push('A')  # 压A入栈
# myStack.push('B')  # 压B入栈
# myStack.push('C')  # 压C入栈
# myStack.push('D')  # 压D入栈
# print(myStack.peek())
# print(myStack.is_empty())  # 判断堆栈是否为空
# print(myStack.pop())  # 将D弹出栈
# print(myStack.pop())  # 将C弹出栈
# print(myStack.pop())  # 将B弹出栈
# print(myStack.get_stack())  # 打印现在的所有栈元素


'''不规则括号问题'''
'''例如‘{【】}’就是匹配的'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
        return self.items[-1]

    def peek(self):
        if self.is_empty():
            return self.items[-1]

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def get_stack(self):
        return self.items


def is_match(p1, p2):  # 判断连续的两个的括号是否匹配
    if p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '(' and p2 == ')':
        return True
    else:
        return False


def is_paren_balance(paren_string):
    s = Stack()  # 创建堆栈来存左括号
    is_balance = True  # 平衡标志当有一组不匹配时就给它赋值False
    index = 0  # 索引输入的每一个括号的序号
    while index in range(len(paren_string)):
        paren = paren_string[index]  # 取每一个括号进行判断
        if paren in "{([":  # 如果它是有括号
            s.push(paren)  # 将它压入栈
        else:
            if s.is_empty():  # 当栈为空时
                is_balance = False  # 必定不平衡
                break
            else:
                top = s.pop()  # 若不为空则将栈头弹出（一定是左括号）
                if not is_match(top, paren):  # 判断是否匹配
                    is_balance = False  # 不匹配时直接标志位置为False
                    break
        index += 1
    if s.is_empty() and is_balance:
        return True
    else:
        return False


print("字符串 : (((({})))) 括号是否平衡匹配?")
print(is_paren_balance("(((({}))))"))

print("字符串2 :{[]}括号是否平衡匹配？")
print(is_paren_balance("{[]}"))


