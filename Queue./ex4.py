class Queue():
    def __init__(self) -> None:
        self.queue = []
    
    def size(self) -> int:
        return len(self.queue)
    
    def is_empty(self) -> bool:
        return not bool(len(self.queue))
    
    def enqueue(self, data: any) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> any:
        if not self.is_empty():
            return self.queue.pop(0)
    
    def front(self) -> any:
        return self.queue[0]
    
    def rear(self) -> any:
        return self.queue[-1]
    
    def __str__(self) -> str:
        return str(self.queue)

print(' ***Cafe***')

s = Queue()
q = Queue()
max_time = -1
max_customer = -1
t = 0

inp = [[i+1,[int(x) for x in e.split(',')]] for i,e in enumerate(input('Log : ').split('/'))]

for i in inp:
    s.enqueue(i)

while (s.size() or q.size()) and t<20:
    if q.size():
        index = 0
        while index < q.size():
            if t == q.queue[index][1]:
                print(f'Time {t} customer {q.queue[index][0]} get coffee ')
                q.queue.pop(index)
            else:
                index += 1
    if s.size():
        while s.size() and t >= s.queue[0][1][0] and q.size() < 2:
            current = s.queue[0]
            q.enqueue([current[0],t+current[1][1]])
            if t-current[1][0]>max_time:
                max_time=t-current[1][0]
                max_customer=current[0]
            s.dequeue()
    t+=1
if max_time <= 0:
    print('No waiting')    
else:
    print(f'The customer who waited the longest is : {max_customer}')
    print(f'The customer waited for {max_time} minutes')

'''
example test cases

 ***Cafe***
Log : 0,3/0,7/2,3/7,7/10,5/10,1
Time 3 customer 1 get coffee  
Time 6 customer 3 get coffee  
Time 7 customer 2 get coffee  
Time 14 customer 4 get coffee  
Time 15 customer 5 get coffee  
Time 15 customer 6 get coffee  
The customer who waited the longest is : 6
The customer waited for 4 minutes

 ***Cafe***
Log : 0,1/1,1/2,1/3,1/4,1/5,1
Time 1 customer 1 get coffee  
Time 2 customer 2 get coffee  
Time 3 customer 3 get coffee  
Time 4 customer 4 get coffee  
Time 5 customer 5 get coffee  
Time 6 customer 6 get coffee  
No waiting

 ***Cafe***
Log : 0,1/0,1/1,1/1,1/2,1/2,1
Time 1 customer 1 get coffee  
Time 1 customer 2 get coffee  
Time 2 customer 3 get coffee  
Time 2 customer 4 get coffee  
Time 3 customer 5 get coffee  
Time 3 customer 6 get coffee  
No waiting
'''
