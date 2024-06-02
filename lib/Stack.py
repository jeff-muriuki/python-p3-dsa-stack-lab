class Stack:
    def __init__(self, items= [], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items)== 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
             
    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit


    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) -1
        except ValueError:
            return -1
