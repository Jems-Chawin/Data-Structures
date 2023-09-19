class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.paths = []

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = new_node
                    break
                elif current.right is None:
                    current.right = new_node
                    break
                else:
                    queue.append(current.left)
                    queue.append(current.right)

    def collection_of_path(self):
        def dfs(node, path):
            if node is None:
                return
            path.append(node.data)
            if node.left is None and node.right is None:
                self.paths.append(list(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        self.paths = []
        dfs(self.root, [])

tree = BinaryTree()

values = [int(x) for x in input("Enter tree: ").split()]
for value in values:
    tree.insert(value)

tree.collection_of_path()

lst = []
for i in tree.paths:
    lst.append(sum(i))
print(f"Maximum path: {tree.paths[lst.index(max(lst))]}")

'''
example test cases
Enter tree: 0 1 2 3 4 5 6
Maximum path: [0, 2, 6]

Enter tree: 0 1 2 3 4 5 4
Maximum path: [0, 2, 5]

Enter tree: 0 1 2 3
Maximum path: [0, 1, 3]

Enter tree: 20 2 3 7 10 0 1
Maximum path: [20, 2, 10]

Enter tree: -1
Maximum path: [-1]
'''
