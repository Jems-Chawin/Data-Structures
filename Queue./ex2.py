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
    
    def extend(self, x):
        return self.queue + x.queue

q = Queue()
s = Queue()
inp = input('Enter Input : ').split(',')
for i in inp :
    if i.split(" ")[0] == "ES":
        s.enqueue(i.split(" ")[1])
    elif i.split(' ')[0] == 'EN':
        q.enqueue(i.split(' ')[1])
    elif i.split(" ")[0] == "D":
        if s.isEmpty() and q.isEmpty():
            print('Empty')
        else :
            if s.size() != 0:
                print(s.dequeue())
            else:
                print(q.dequeue())

'''
example test cases

Enter Input : EN 1,EN 2,D,D,D,EN 3,D
1
2
Empty
3

Enter Input : EN 1,ES 2,D,D,D,EN 3,D
2
1
Empty
3

Enter Input : EN 1,ES 2,ES 99,D,D,D,EN 3,D
2
99
1
3
'''
