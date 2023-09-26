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
        queue = [root]

        while queue:
            current = queue.pop(0)  # Dequeue the front node

            # Check left child for insertion
            if not current.left:
                current.left = TreeNode(key)
                break  # Inserted, so break out of the loop
            else:
                queue.append(current.left)

            # Check right child for insertion
            if not current.right:
                current.right = TreeNode(key)
                break  # Inserted, so break out of the loop
            else:
                queue.append(current.right)
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
 
    def update_and_sum(self,root):
        def update(node):
            if node is None:
                return 0
            left_sum = update(node.left)
            right_sum = update(node.right)
            
            # Check if both left and right children exist
            if node.left and node.right:
                # Find the minimum value among the children and update the parent node
                min_child_value = min(node.left.val, node.right.val)
                node.val = min_child_value
                return left_sum + right_sum + node.val -2*min_child_value
            return left_sum + right_sum + node.val 

        if root:
            total_sum = update(root)
            return total_sum
        else:
            return 0
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
myTree = AVL_Tree() 
root = None
amount,val = input("Enter Input : ").strip().split("/")
amount = int(amount)
val = [int(x) for x in val.split(" ")]
if amount//2+1 != len(val):
    print("Incorrect Input")
else:
    for i in ([0]*(amount-len(val))+val):
        try:
            root = myTree.insert(root,i)
        except ValueError:
            pass
    # printTree90(root)
    print(myTree.update_and_sum(root))

'''
example test cases
Enter Input : 7/1 2 3 4
5

Enter Input : 7/1 2 3 4 5
Incorrect Input

Enter Input : 9/5 5 5 5 5
5
'''