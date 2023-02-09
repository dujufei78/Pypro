#-*- encoding: utf-8 -*-
## __enter__和__exit__方法
# 上下文管理器：内部实现了__enter__和__exit__方法的对象，都可以叫做上下文管理器
class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('......in inter.....')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print('.....in exit.......')
        self.f.close()


with File('out.txt', 'w') as f:
    print('......writing......')
    f.write('hello, 2b....')


## __repr__和__str__语法
# __repr__是面向开发者，后者面向用户

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return '.'.join(self.employee)
    # def __repr__(self): # 可以自己写
    #     return '-'.join(self.employee)


company = Company(['dujufei', 'siqi', 'yangshi'])
print(company)  # 用户模式打印出了：  dujufei.siqi.yangshi
# 使用开发者模式，cmd里输入代码，输入company,默认调用的__repr__方法，打印出了：<__main__.Company object at 0x0000015ABB78DC70>
# 当然，__repr__方法也可以自己写，如上，cmd里输入代码，输入company，打印出了：dujufei-siqi-yangshi