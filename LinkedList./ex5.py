class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self, lst=[]):
        
        self.head = None
        self.tail = None
        self.size = 0
        if lst != []:
            for num in lst:
                self.append(Node(num))
      
    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        
        return node

    def prepend(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1
        return node

    def __deleteOne(self):
        temp = self.head
        self.head = None 
        self.tail = None
        self.size -= 1
        return temp
    
    def pop(self):
        if self.head == None:
            return None 
        if self.head == self.tail:
            return self.__deleteOne()
        last = self.tail 
        self.tail = self.tail.prev
        self.tail.next = None
        last.prev = None
        self.size -= 1
        return last
    
    def popLeft(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            return self.__deleteOne()
        left = self.head
        self.head = self.head.next
        self.head.prev = None
        left.next = None
        self.size -= 1
        return left
    
    def moveToHeadRev(self, ll2):
        while ll2.head:
            self.prepend(ll2.popLeft())
            
    def moveToHead(self, ll2):
        while ll2.tail:
            self.prepend(ll2.pop())
    
    def isEmpty(self):
        return self.head == None
    
    def out(self):
        res = ""
        cur = self.head 
        while cur != None:
            res += str(cur.val) + " -> "
            cur = cur.next
        return res[:-4]
    
    def printBackward(self):
        res = ""
        cur = self.tail
        while cur != None:
            res += str(cur.val) + " "
            cur = cur.prev
        return res
    
    def __str__(self):
        res = ""
        cur = self.head 
        while cur != None:
            res += str(cur.val) + " "
            cur = cur.next
        return res
    
    def __len__(self):
        return self.size
    
def countDigit(num):
    num = abs(num)
    i=0
    while num > 0:
        num = num//10
        i+=1
    return i

def getMaxDigit(nums):
    max = 0
    for num in nums:
        digits = countDigit(num)
        if digits > max:
            max = digits
    return max

def getNumAt(digit, num):
    num = abs(num)
    i=0
    res = -1
    while i<digit:
        res = num%10
        num = num//10
        i+=1
    return res
    
def radixSort(nums):
    max_digit = getMaxDigit(nums)
    length = len(nums)
    check = 0
    ll = LinkedList(nums)
    pos = [LinkedList() for i in range(10)]
    neg = [LinkedList() for i in range(10)]
    before = "Before Radix Sort : " + ll.out()
    
    for digit in range(1, max_digit+2):
        while not ll.isEmpty():
            node = ll.popLeft()
            num = node.val
            index = getNumAt(digit, num)
            if num<0:
                neg[index].append(node)
            else:
                pos[index].append(node)
        if digit == max_digit+1: 
            for i in range(10):
                ll.moveToHeadRev(neg[i])
                ll.moveToHead(pos[i])
            break
        print(f"Round : {digit}")
        for i in range(10):
            print(f"{i} : {pos[i]}{neg[i].printBackward()}")
            ll.moveToHead(neg[i])
            ll.moveToHead(pos[i])
        print("------------------------------------------------------------")
    print(f"{digit-1} Time(s)")
    print(before)
    print(f"After  Radix Sort : {ll.out()}")
    
#driver
inp = input("Enter Input : ").split()
nums = [int(x) for x in inp]
print("------------------------------------------------------------")
radixSort(nums)




# ไล่มากไปน้อย
#     ออกที่head
#     ใช้2Likedlist per digit
#     if positive:
#         เข้าที่tail positive
#     elif negative:
#         เข้าที่ head negative
# positive.tail.next = negative.head

'''
example test cases

Enter Input : 64 8 216 512 27 729 0 1 343 125
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 
2 : 512 
3 : 343 
4 : 64 
5 : 125 
6 : 216 
7 : 27 
8 : 8 
9 : 729 
------------------------------------------------------------
Round : 2
0 : 8 1 0 
1 : 216 512 
2 : 729 27 125 
3 : 
4 : 343 
5 : 
6 : 64 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 64 27 8 1 0 
1 : 125 
2 : 216 
3 : 343 
4 : 
5 : 512 
6 : 
7 : 729 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0

Enter Input : 456 -789 0 -50384 15615 -1 72
------------------------------------------------------------
Round : 1
0 : 0 
1 : -1 
2 : 72 
3 : 
4 : -50384 
5 : 15615 
6 : 456 
7 : 
8 : 
9 : -789 
------------------------------------------------------------
Round : 2
0 : 0 -1 
1 : 15615 
2 : 
3 : 
4 : 
5 : 456 
6 : 
7 : 72 
8 : -50384 -789 
9 : 
------------------------------------------------------------
Round : 3
0 : 72 0 -1 
1 : 
2 : 
3 : -50384 
4 : 456 
5 : 
6 : 15615 
7 : -789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 456 72 0 -1 -50384 -789 
1 : 
2 : 
3 : 
4 : 
5 : 15615 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 5
0 : 456 72 0 -1 -789 
1 : 15615 
2 : 
3 : 
4 : 
5 : -50384 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : 456 -> -789 -> 0 -> -50384 -> 15615 -> -1 -> 72
After  Radix Sort : 15615 -> 456 -> 72 -> 0 -> -1 -> -789 -> -50384

Enter Input : -12345 98765 -87654
------------------------------------------------------------
Round : 1
0 : 
1 : 
2 : 
3 : 
4 : -87654 
5 : 98765 -12345 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 2
0 : 
1 : 
2 : 
3 : 
4 : -12345 
5 : -87654 
6 : 98765 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 
1 : 
2 : 
3 : -12345 
4 : 
5 : 
6 : -87654 
7 : 98765 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 
1 : 
2 : -12345 
3 : 
4 : 
5 : 
6 : 
7 : -87654 
8 : 98765 
9 : 
------------------------------------------------------------
Round : 5
0 : 
1 : -12345 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : -87654 
9 : 98765 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : -12345 -> 98765 -> -87654
After  Radix Sort : 98765 -> -12345 -> -87654
'''
