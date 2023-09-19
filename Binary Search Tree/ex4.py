class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, current, val):
        if val < current.data:
            if current.left is None:
                current.left = Node(val)
            else:
                self._insert(current.left, val)
        elif val > current.data:
            if current.right is None:
                current.right = Node(val)
            else:
                self._insert(current.right, val)
        else:
            print(f"insert {val} already exists")

    def search(self,data):
        if self.root!=None:
            return self._search(data,self.root)
        else:
            return False
        
    def _search(self,data,cur_node):
        if data==cur_node.data:
            return True
        elif data<cur_node.data and cur_node.left!=None:
            return self._search(data,cur_node.left)
        elif data>cur_node.data and cur_node.right!=None:
            return self._search(data,cur_node.right)
        return False

    def delete(self, data):
        if self.root is None:
            print("Error! Not Found DATA")
        elif self.search(data)==False:
            print("Error! Not Found DATA")
        else:
            self.root = self._delete(self.root, data)

    def _delete(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete(current.left, data)
        elif data > current.data:
            current.right = self._delete(current.right, data)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            min_val = self._find_min_value(current.right)
            current.data = min_val
            current.right = self._delete(current.right, min_val)

        return current

    def _find_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data


def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for command in data:
    command = command.split()
    if command[0] == 'i':
        value = int(command[1])
        tree.insert(value)
        print(f"insert {value}")
        printTree90(tree.root)
    elif command[0] == 'd':
        value = int(command[1])
        print(f"delete {value}")
        tree.delete(value)
        printTree90(tree.root)

'''
example test cases
Enter Input : i 3,i 5,i 2,d 3
insert 3
 3
insert 5
      5
 3
insert 2
      5
 3
      2
delete 3
 5
      2

Enter Input : d 1,i 1,d 1,i 0,i 2,i 4,i 1,i 5,i 3,d 2
delete 1
Error! Not Found DATA
insert 1
 1
delete 1
insert 0
 0
insert 2
      2
 0
insert 4
           4
      2
 0
insert 1
           4
      2
           1
 0
insert 5
                5
           4
      2
           1
 0
insert 3
                5
           4
                3
      2
           1
 0
delete 2
                5
           4
      3
           1
 0

Enter Input : i 8,i 7,d 1,i 3,i 1,i 2,i 6,i 9,d 8,d 9,d 7,d 1,d 6,d 3,d 2
insert 8
 8
insert 7
 8
      7
delete 1
Error! Not Found DATA
 8
      7
insert 3
 8
      7
           3
insert 1
 8
      7
           3
                1
insert 2
 8
      7
           3
                     2
                1
insert 6
 8
      7
                6
           3
                     2
                1
insert 9
      9
 8
      7
                6
           3
                     2
                1
delete 8
 9
      7
                6
           3
                     2
                1
delete 9
 7
           6
      3
                2
           1
delete 7
      6
 3
           2
      1
delete 1
      6
 3
      2
delete 6
 3
      2
delete 3
 2
delete 2
'''
