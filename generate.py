import sys
import random

sizeOfPattern = int(sys.argv[1])
sizeOfAlphabet = int(sys.argv[2])
sizeOfText = int(sys.argv[3])
seed = int(sys.argv[4])

random.seed(seed)

TERMINALS = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]
OPERATORS = ['*', '', '|']

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
        root.chars = prefix + random.choice(TERMINALS) + ('*' if random.random() < 0.05 else '') + suffix
        return root
    
    left_size = random.randint(1, size-1)
    right_size = size - left_size

    if random.random() < 0.1:
        root.chars = prefix + '.*' + suffix
        root.left = generate_tree(left_size)
        root.right = generate_tree(right_size)
    elif random.random() < 0.1 and len(prefix) == 0 and len(suffix) == 0:
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


print(''.join(random.choices(TERMINALS, k=sizeOfText)))
regex_tree = generate_tree(sizeOfPattern)
print(traversal(regex_tree))
