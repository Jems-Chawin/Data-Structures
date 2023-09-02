# 2D - Link List 

class node:
    def __init__(self,data,next=None,next_s=None):
        self.data = data
        self.next = next
        self.next_s = next_s

class Snode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class link:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def next_node(self,data):
        n = node(data)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def search(self,data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur.data
            cur = cur.next
        return None

    def search_s(self,data):
        cur = self.head
        while cur:
            cur_s = cur.next_s
            while cur_s:
                if cur_s.data == data:
                    return cur_s.data
                cur_s = cur_s.next
            cur = cur.next
        return None

    def next_secondary_node(self, n, data):
        s = Snode(data)
        cur = self.head
        while cur:
            if cur.data == n:
                if cur.next_s is None:
                    cur.next_s = s
                else:
                    cur_s = cur.next_s
                    while cur_s.next:
                        cur_s = cur_s.next
                    cur_s.next = s
            cur = cur.next

    def show_all(self):
        cur = self.head
        while cur:
            print(cur.data, end=' : ')
            cur_s = cur.next_s
            while cur_s:
                print(cur_s.data, end=',')
                cur_s = cur_s.next
            cur = cur.next
            print()

def main():
    inp = input('input : ').split(',')
    L = link()
    for i in inp:
        if i[:3] == 'ADN':
            if L.search(i[-1]) is None:
                L.next_node(i[-1])
        elif i[:4] == 'ADSN':
            if L.search_s(i[-2::]) is None:
                L.next_secondary_node(i[-4],i[-2::])
    L.show_all()
    

if __name__ == '__main__':
    main()

'''
example test cases

input : ADN A,ADN B,ADSN A-A1,ADSN A-A2,ADSN A-A3
A : A1,A2,A3,
B : 

input : ADN A,ADN B,ADN C,ADN D,ADSN A-A1,ADN A
A : A1,
B : 
C : 
D : 
'''
