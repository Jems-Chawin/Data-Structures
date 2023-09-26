class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
        return str(self.val)
class AVL_Tree(object):

    def insert(self, root, key):
         
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)

    def search(self,root, key):
        if root is None:
            return False 
        if key == root.val:
            return root  

        if key < root.val:
            return self.search(root.left, key)  

        return self.search(root.right, key) 

def burn_tree_util(root, target, q):
    # Base condition
    if root is None:
        return 0
 
    # Condition to check whether target
    # node is found or not in a tree
    if root.val == target:
        print(root)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
 
        # Return statements to prevent
        # further function calls
        return 1
 
    a = burn_tree_util(root.left, target, q)
 
    if a == 1:
        q_size = len(q)
 
        # Run while loop until size of queue
        # becomes zero
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp, end=" ")
            del q[0]
 
            # Check if condition for left subtree
            if temp.left is not None:
                q.append(temp.left)
 
            # Check if condition for right subtree
            if temp.right is not None:
                q.append(temp.right)
 
            q_size -= 1
 
        if root.right is not None:
            q.append(root.right)
 
        print(root)
 
        # Return statement it prevents further
        # further function call
        return 1
 
    b = burn_tree_util(root.right, target, q)
 
    if b == 1:
        q_size = len(q)
        # Run while loop until size of queue
        # becomes zero
 
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp, end=" ")
            del q[0]
 
            # Check if condition for left subtree
            if temp.left is not None:
                q.append(temp.left)
 
            # Check if condition for left subtree
            if temp.right is not None:
                q.append(temp.right)
 
            q_size -= 1
 
        if root.left is not None:
            q.append(root.left)
 
        print(root)
 
        # Return statement it prevents further
        # further function call
        return 1
 
# Function will print the sequence of burning nodes
def burn_tree(root, target):
    q = []
 
    # Function call
    burn_tree_util(root, target, q)
 
    # While loop runs unless queue becomes empty
    while q:
        q_size = len(q)
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp, end="")
            # Insert left child in a queue, if exist
            if temp.left is not None:
                q.append(temp.left)
            # Insert right child in a queue, if exist
            if temp.right is not None:
                q.append(temp.right)
 
            if len(q) != 1:
                print(" ", end="")
 
            del q[0]
            q_size -= 1
        print()

myTree = AVL_Tree()
root = None
num,burn = input("Enter node and burn node : ").strip().split("/")
for i in num.split(" "):
    try:
        root = myTree.insert(root, int(i.strip()))
    except ValueError:
        pass
burn = int(burn)
if myTree.search(root,burn):
    burn_tree(root, burn)
else:
    print(f"There is no {burn} in the tree.")
    
'''
example test cases
Enter node and burn node : 12 14 21 22 13 15 10 23 24/14
14
12 21 
10 13 15 23 
22 24 

Enter node and burn node : 2 234 16 643/-234
There is no -234 in the tree.

Enter node and burn node : 1 2 3 4 5 6 7 8 9 0 10 11/0
0
1
2
3 4
8 
6 10 
5 7 9 11 
'''