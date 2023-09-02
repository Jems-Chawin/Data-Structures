class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def enqueue(self, i):
        self.queue.append(i)

    def dequeue(self):
        if self.isEmpty() is not True:
            return self.queue.pop(0)
        else: 
            return -1
        
    def count(self, i):
        return self.queue.count(i)
    
    def check_duplicate(self):
        for i in self.queue:
            if self.queue.count(i) > 1:
                return 'Duplicate'
        return 'NO Duplicate'

q = Queue()
s = Queue()
inp = input('Enter Input : ').split('/')
str1 = inp[0]
str2 = inp[1]
queue = [i for i in str1.split()]
stock = [i for i in str2.split(',')]
for i in queue:
    q.enqueue(i)
for i in stock:
    s.enqueue(i)
for i in s.queue:
    if i.split(" ")[0] == "E":
        q.enqueue(i.split(" ")[1])
    elif i.split(" ")[0] == "D":
        q.dequeue()
print(q.check_duplicate())

'''
example test cases

Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate
'''
