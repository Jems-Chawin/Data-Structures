class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def addHead(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

    def insert(self, pos, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
            self.tail = node
        elif pos == 0:
            self.head.previous = node
            node.next = self.head
            self.head = node
        elif pos > 0:
            cur = self.head
            count = 0
            while cur.next and count < (pos - 1):
                cur = cur.next
                count += 1

            if count < (pos - 1):
                cur.next = node
                node.previous = cur
                self.tail = node
            else:
                node.next = cur.next
                node.previous = cur
                cur.next = node
                if node.next:
                    node.next.previous = node
        elif pos < 0:
            cur = self.tail
            count = -1
            while cur.previous and count > pos:
                cur = cur.previous
                count -= 1

            if count == pos - 1:
                cur.previous = node
                node.next = cur
                self.head = node

            elif count > pos:
                cur.previous = node
                node.next = cur
                self.head = node

            else:
                node.previous = cur.previous
                node.next = cur
                cur.previous = node
                if node.previous:
                    node.previous.next = node

    def search(self, item):
        cur = self.head
        while cur:
            if cur.value == item:
                return 'Found'
            cur = cur.next
        return 'Not Found'

    def index(self, item):
        cur = self.head
        index = 0
        while cur:
            if cur.value == item:
                return index
            cur = cur.next
            index += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if pos < 0 or pos >= self.size():
            return ("Out of Range")

        if pos == 0:
            popped_value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
        else:
            cur = self.head
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            popped_value = cur.next.value
            cur.next = cur.next.next
            if cur.next:
                cur.next.previous = cur
            else:
                self.tail = cur

        return 'Success'
