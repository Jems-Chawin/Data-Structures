class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []
    
    def elements(self):
        return self.stack
    
    def mushroom(self):
        new_height = Stack()
        while not self.is_empty():
            if self.peek() % 2 == 0:
                new_height.push(self.pop()-1)
            else:
                new_height.push(self.pop()+2)
        while not new_height.is_empty():
            self.push(new_height.pop())
        return True
    
    def lookback(self):
        tree_amount = Stack()
        for height in self.elements():
            while not tree_amount.is_empty() and tree_amount.peek() <= height:
                tree_amount.pop()
            tree_amount.push(height)
        return tree_amount.size()

S = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i == 'B':
        print(S.lookback())
    elif i == 'S':
        S.mushroom()
    else:
        height = int((i.split(' '))[1])
        S.push(height)

'''
example test cases

Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
2
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
2
1
1
1
'''
