#-*- encoding: utf-8 -*-
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

        return None

    def deleteHead(self) -> int:  # 考虑队列先入先出
        val = -1
        if len(self.stack2):
            val = self.stack2.pop()
        else:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            if self.stack2:
                val = self.stack2.pop()

        return val


# Your CQueue object will be instantiated and called as such:
value = 111

obj = CQueue()
obj.appendTail(value)
param_2 = obj.deleteHead()