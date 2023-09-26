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
            current.height = 1 + max(self.getHeight(current.left),
                            self.getHeight(current.right))
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
 
    def compare(self,root,lst):
        for x in lst.split(","):
            first,second = [int(i) for i in x.split(" ")]
            sum1 = self.sumAll(self.searchByPos(root,first))
            sum2 = self.sumAll(self.searchByPos(root,second))
            if sum1 < sum2:
                print(f"{first}<{second}")
            elif sum1 == sum2:
                print(f"{first}={second}")
            else:
                print(f"{first}>{second}")
    def sumAll(self,node):
        if node is None:
            return 0
        left_sum = self.sumAll(node.left)
        right_sum = self.sumAll(node.right)
        return left_sum + right_sum + node.val 
    def searchByPos(self,root, pos):
        if not root:
            return None
        else:
            queue = [root]
            count = 0
            while queue:
                current = queue.pop(0)
                if count == pos:
                    return current
                if current.left and current.right:
                    queue.append(current.left)
                    queue.append(current.right)  
                count += 1
            return None
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node.val)
            self.printTree(node.left, level + 1)

myTree = AVL_Tree() 
root = None
armys,compare = input("Enter Input : ").strip().split("/")
for army in armys.split(" "):
    try:
        root = myTree.insert(root, int(army.strip()))
    except ValueError:
        pass
print(myTree.sumAll(root))
myTree.compare(root,compare)

'''
example test cases
Enter Input : 5 4 4 3 2 2 2/1 2,5 6,2 0
22
1>2
5=6
2<0

Enter Input : 4 5/0 1,1 0
9
0>1
1<0
'''