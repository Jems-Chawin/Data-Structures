class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        if self.size()>0:
            return self.items[-1] 
        else:
            return -1

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()
    
    def boom(self):
        lst = []
        n = 0
        for i in self.items:
            lst.append(i)
            if len(lst) > 2 and len(set(lst[-3:])) == 1:
                del lst[-3:]
                n += 1
        return len(lst)
        
    def renew(self):
        lst = []
        rev = []
        for i in self.items:
            lst.append(i)
            if len(lst) > 2 and len(set(lst[-3:])) == 1:
                del lst[-3:]
        for i in range(len(lst)):    
            rev.append(lst.pop())
        if len(rev) != 0:
            return ''.join(rev)
        else:
            return 'Empty'

    def combo(self):
        lst = []
        n = 0
        for i in self.items:
            lst.append(i)
            if len(lst) > 2 and len(set(lst[-3:])) == 1:
                del lst[-3:]
                n += 1
        if n > 1:
            return f'Combo : {n} ! ! !'
        else:
            return ''

inp = input('Enter Input : ').split()

S = Stack()

'''
example test cases

Enter Input : G H H H H P
3
PHG

Enter Input : L C C X X X C D
2
DL
Combo : 2 ! ! !

Enter Input : C C C
0
Empty

Enter Input : A B B A
4
ABBA

Enter Input : O O P Y Y E R R R E E Y P P K K K O
0
Empty
Combo : 6 ! ! !
'''
