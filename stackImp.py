class stack:
    def __init__(self):
        self.top = []
    
    def push(self, data):
        self.top.append(data)
    
    def pop(self):
        if len(self.top):
            return self.top.pop()
        return "Stack is empty"
    def peek(self):
        if len(self.top):
            return self.top[-1]
        return "Stack is empty"
    
    def size(self):
        return len(self.top)
    
    def isEmpty(self):
        return not(len(self.top))