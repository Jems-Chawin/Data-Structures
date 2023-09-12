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
        if self.root==None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left==None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right==None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("data already exist")

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)  # Call the insert method on the BST instance
T.printTree(T.root)

'''
example test cases
Enter Input : 10 4 20 1 5
      20
 10
           5
      4
           1

Enter Input : 4 10 3 6 13 9
           13
      10
                9
           6
 4
      3

Enter Input : 1 2 3 4 5 6 7 8 0 -1 -2
                                    8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2
'''
