class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
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
            if cur_node.left_child==None:
                cur_node.left_child=Node(data)
            else:
                self._insert(data,cur_node.left_child)
        elif data>cur_node.data:
            if cur_node.right_child==None:
                cur_node.right_child=Node(data)
            else:
                self._insert(data,cur_node.right_child)
        else:
            print("data already exist")

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.data),end=' ')
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0
        
    def _height(self,cur_node,cur_height):
        if cur_node==None:
            return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
    
    def search(self,data):
        if self.root!=None:
            return self._search(data,self.root)
        else:
            return False
        
    def _search(self,data,cur_node):
        if data==cur_node.data:
            return True
        elif data<cur_node.data and cur_node.left_child!=None:
            return self._search(data,cur_node.left_child)
        elif data>cur_node.data and cur_node.right_child!=None:
            return self._search(data,cur_node.right_child)
        return False

tree = BST()
inp = input("Enter Input : ").split()
for i in inp:
    tree.insert(i)
# tree.print_tree()
print(f"Height of this tree is : {tree.height() - 1}")