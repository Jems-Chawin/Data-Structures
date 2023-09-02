class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        del self.items[-1]
    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)



print(' *** Stack implement by Python list***')

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)

'''
example test cases

 *** Stack implement by Python list***
Enter data to stack : K M I T L C E 2 5 6 3
11 Data in stack :  ['K', 'M', 'I', 'T', 'L', 'C', 'E', '2', '5', '6', '3']
0 Data in stack :  []

 *** Stack implement by Python list***
Enter data to stack : 1.24 2.365 3653.2563 325336.2556 .3625 .35465 .85484
7 Data in stack :  ['1.24', '2.365', '3653.2563', '325336.2556', '.3625', '.35465', '.85484']
0 Data in stack :  []

 *** Stack implement by Python list***
Enter data to stack : we are computer engineer. I love KMITL.
7 Data in stack :  ['we', 'are', 'computer', 'engineer.', 'I', 'love', 'KMITL.']
0 Data in stack :  []
'''
