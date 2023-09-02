class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            if current_node.next == None:
                print(current_node.data,end='')
                break
            else:
                print(current_node.data, end=' <- ')
                current_node = current_node.next
        print("",end='')

    def remove(self, data):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
        
    def insert(self, position, data):
        new_node = Node(data)
        if position == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(position - 1):
            if current_node.next is None:
                raise IndexError("Position out of range")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

print(' *** Locomotive ***')

lst = LinkedList()
head = LinkedList()
tail = LinkedList()

inp = input('Enter Input : ').split(' ')

for i in inp:
    lst.append(i)

first = []
second = []
for i in inp:
    if i != '0':
        second.append(i)
    else:
        break
first = [i for i in inp if i not in second]
for i in first:
    head.append(i)
for i in second:
    tail.append(i)

if second == []:
    print('Before : ',end='')
    lst.display()
    print()
    print('After : ',end='')
    lst.display()

else:
    print('Before : ',end='')
    lst.display()
    print()
    print('After : ',end='')
    head.display()
    print(' <- ',end='')
    tail.display()

'''
example test cases

 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1

 *** Locomotive ***
Enter Input : 5 4 3 2 1 0 9 8 7 6
Before : 5 <- 4 <- 3 <- 2 <- 1 <- 0 <- 9 <- 8 <- 7 <- 6
After : 0 <- 9 <- 8 <- 7 <- 6 <- 5 <- 4 <- 3 <- 2 <- 1

 *** Locomotive ***
Enter Input : 1 0
Before : 1 <- 0
After : 0 <- 1

 *** Locomotive ***
Enter Input : 0 1 2 3 4 5 6 7 8 9
Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9

 *** Locomotive ***
Enter Input : 2 0 1
Before : 2 <- 0 <- 1
After : 0 <- 1 <- 2
'''
