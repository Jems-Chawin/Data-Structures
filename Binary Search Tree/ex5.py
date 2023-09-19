class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left is not None:
            return self._search(data, cur_node.left)
        elif data > cur_node.data and cur_node.right is not None:
            return self._search(data, cur_node.right)
        return False

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, data):
        if self.search(data) == False:
            print("Not exist")
        elif self.root.data == data:
            print("Root")
        else:
            result = self._checkpos(self.root, data)
            if result == "Leaf":
                print("Leaf")
            elif result == "Inner":
                print("Inner")

    def _checkpos(self, node, data):
        if node is None:
            return "Not exist"
        if data == node.data:
            if node.left is not None and node.right is not None:
                return "Inner"
            else:
                return "Leaf"
        elif data < node.data:
            return self._checkpos(node.left, data)
        else:
            return self._checkpos(node.right, data)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    T.insert(inp[i])
T.printTree(T.root)
T.checkpos(inp[0])

'''
example test cases
Enter Input : 30 10 4 20 1 5
      20
 10
           5
      4
           1
Not exist

Enter Input : 4 4 10 3 6 13 9
           13
      10
                9
           6
 4
      3
Root

Enter Input : 10 7 10 3 6 13 9
           13
      10
           9
 7
           6
      3
Inner
'''
