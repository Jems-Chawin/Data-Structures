class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l:
        return None
    head = Node(l[0])
    current = head
    for i in range(1, len(l)):
        node = Node(l[i])
        current.next = node
        current = current.next
    return head

def printList(H):
    current = H
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

def mergeOrderedLists(p, q):
    if p is None:
        return q
    if q is None:
        return p

    dummy = Node(0)
    current = dummy

    while p is not None and q is not None:
        if p.data <= q.data:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next

        current = current.next

    if p is not None:
        current.next = p
    else:
        current.next = q

    return dummy.next



def main():
    inp = input('Enter 2 Lists : ').split()
    L1 = [int(i) for i in inp[0].split(',')]
    L2 = [int(i) for i in inp[1].split(',')]

    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ', end='')
    printList(LL1)
    print('LL2 : ', end='')
    printList(LL2)
    m = mergeOrderedLists(LL1, LL2)
    print('Merge Result : ', end='')
    printList(m)

if __name__ == '__main__':
    main()

'''
example test cases

Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 

Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
LL1 : 1 4 5 5 6 7 
LL2 : 2 3 6 9 10 
Merge Result : 1 2 3 4 5 5 6 6 7 9 10 

Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
LL1 : 2 2 2 10 
LL2 : 1 1 1 1 5 5 5 6 7 8 
Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10 
'''
