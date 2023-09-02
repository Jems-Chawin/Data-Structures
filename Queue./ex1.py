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

q = Queue()
inp = input('Enter Input : ').split(',')

for i in inp :
    if i.split(" ")[0] == "E":
        q.enqueue(i.split(" ")[1])
        print(q.size())
    elif i.split(" ")[0] == "D":
        if q.isEmpty() :
            print(-1)
        else :
            print(q.dequeue() + " 0")
if q.isEmpty():
    print("Empty") 
else :
    print(' '.join(q.queue))   

'''
example test cases

Enter Input : E 10,E 20,E 30,E 40,D,D
1
2
3
4
10 0
20 0
30 40

Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
1
2
3
4
10 0
4
5
20 0
30 0
40 0
50 0
60 0
-1
Empty
'''
