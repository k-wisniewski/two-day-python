class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def divisible_by_three_dfs(node):
    if node is not None:
        if node.value % 3 == 0:
            yield node.value
        yield from divisible_by_three_dfs(node.left)
        yield from divisible_by_three_dfs(node.right)

# Przykładowe użycie:
# Zbuduj drzewo
root = Node(1, Node(3), Node(6, Node(5), Node(9)))

# Użyj generatora do znalezienia wartości podzielnych przez 3
for value in divisible_by_three_dfs(root):
    print(value)

