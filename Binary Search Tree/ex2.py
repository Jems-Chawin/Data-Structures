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
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left_child is None:
                cur_node.left_child = Node(data)
            else:
                self._insert(data, cur_node.left_child)
        elif data > cur_node.data:
            if cur_node.right_child is None:
                cur_node.right_child = Node(data)
            else:
                self._insert(data, cur_node.right_child)
        else:
            raise ValueError("Data already exists in the tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.data), end=' ')
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return -1  # Return -1 for an empty tree

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left_child is not None:
            return self._search(data, cur_node.left_child)
        elif data > cur_node.data and cur_node.right_child is not None:
            return self._search(data, cur_node.right_child)
        return False

if __name__ == "__main__":
    tree = BST()
    inp = input("Enter Input : ").split()
    for i in inp:
        tree.insert(int(i))  # Assuming you want to insert integers
    print(f"Height of this tree is : {tree.height()-1}")

'''
example test cases
Enter Input : 3 5 2 1 4 6
Height of this tree is : 2

Enter Input : 3 5 2 1 4 6 7
Height of this tree is : 3

Enter Input : 1
Height of this tree is : 0
'''
