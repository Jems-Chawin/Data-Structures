class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def max(self):
        return max(self.items)
    
    def reverse(self):
        return self.items.reverse()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    
    def top(self):
        return self.items[-1] if self.size() > 0 else -1

    def count_tree(self):
        tree = []
        tree.append(self.items.pop())
        return tree

S = Stack()
T = Stack()
K = Stack()
R = Stack()
N = Stack()

inp = input('Enter Input : ').split(',')
for i in inp:
    S.push(i)
for i in S.items:
    if i == 'B':
        print(0)
        continue
    else:
        break
while S.top() != 'B':
    S.pop()
S.pop()
while S.isEmpty() == False and S.top() != 'B':
    t = int([int(i.split()[1]) for i in S.count_tree()][0])
    T.push(t)
    if S.isEmpty() == True:
        K.push(T.items[::])
        break
    while S.top() == 'B':
        K.push(T.items[::])
        S.pop()

while K.isEmpty() == False:
    lst1 = K.items[-1]
    lst2 = K.items[-2]
    for i in lst2:
        if i in lst1:
            lst1.remove(i)
    R.push(lst1[::])
    K.pop()
    if R.size() > 1:
        R.items[-1] = list(R.items[-1] + R.items[-2])
    if K.size() == 1:
        R.push(T.items)
        break
      
for i in R.items:
    if len(i) == 0:
        continue
    for j in i:
        if N.isEmpty() == True:
            N.push(j)
        while j>N.max():
            N.push(j)
    print(N.size())
    N.items = []

'''
example test cases

Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

Enter Input : B,B,B,A 10,A 1,A 3,A 2,B,A 1,A 1,B,A 5,A 4,B
0
0
0
3
4
3

Enter Input : A 100,A 50,A 25,A 12,A 6,B,B,B,A 76,B,A 61,B,A 1,B,B,A 6,A 11,B
5
5
5
2
3
4
4
4

Enter Input : A 1,A 2,A 3,A 4,B,A 3,A 2,B,A 99,A 5,B,A 4,B,A 67
1
3
2
3
'''
