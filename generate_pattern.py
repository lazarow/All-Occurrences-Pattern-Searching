import sys
import random

sizeOfPattern = int(sys.argv[1])
sizeOfAlphabet = int(sys.argv[2])
seed = int(sys.argv[3])
justPattern = bool(sys.argv[4] if len(sys.argv) >= 5 else 0)

random.seed(seed)

TERMINALS = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]

class Node:
    def __init__(self, chars=''):
        self.chars = chars
        self.left = None
        self.right = None

def generate_tree(size, prefix='', suffix=''):
    
    if size <= 0:
        return None
        
    root = Node()
    
    if size == 1:
        root.chars = prefix + random.choice(TERMINALS) + suffix
        return root
    
    left_size = random.randint(1, size-1)
    right_size = size - left_size

    if random.random() < 0.075:
        root.chars = prefix + '.*' + suffix
        root.left = generate_tree(left_size)
        root.right = generate_tree(right_size)
    elif random.random() < 0.2 and len(prefix) == 0 and len(suffix) == 0:
        root.chars = prefix + '|' + suffix
        root.left = generate_tree(left_size, '(', '')
        root.right = generate_tree(right_size, '', ')')
    else:
        root.chars = prefix + '' + suffix
        root.left = generate_tree(left_size)
        root.right = generate_tree(right_size)
    
    return root

def traversal(node):
    if node is None:
        return ''
    return traversal(node.left) + node.chars + traversal(node.right)

regex_tree = generate_tree(sizeOfPattern)
print(traversal(regex_tree))
