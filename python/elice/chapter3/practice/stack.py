class Stack:
    def __init__(self):
        self.list = []
 
    def push(self, num):
        self.list.append(num)
 
    def pop(self):
        if self.size() == 0:
            return -1
        return self.list.pop()
 
    def size(self):
        return len(self.list)
 
    def empty(self):
        return 1 if len(self.list) == 0 else 0
 
    def top(self):
        return self.list[-1] if self.size() != 0 else -1


# 스택을 굳이 클래스로 만든다면 이렇게 만들 수 있다. 