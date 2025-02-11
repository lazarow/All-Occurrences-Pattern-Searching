import json
import random
from sys import platform

if platform == "linux" or platform == "linux2":
    pythonCommand = "python3"
else:
    pythonCommand = "python"

dataset = 1
with open('configurations.json', 'r') as file:
    configurations = json.load(file)
    for configuration in configurations:
        numberOfRegexes = int(configuration[0])
        sizeOfAlphabet = int(configuration[1])
        sizeOfText = int(configuration[2])
        seed = int(configuration[3])
        
        random.seed(seed)

        f = open("datasets/dataset" + (str(dataset).rjust(2, '0')) + ".txt", "w")

        letters = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]
        separator = chr(ord('a') + sizeOfAlphabet)

        text = separator
        while len(text) < sizeOfText:
            word_size = random.randint(10, 50)
            random_string = ''.join(random.choices(letters, k=word_size))
            text += random_string + separator

        f.write(text + "\n")

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
                if random.random() < 0.01:
                    root.chars = prefix + random.choice(letters) + "*" + suffix
                elif random.random() < 0.01:
                    root.chars = prefix + random.choice(letters) + "+" + suffix
                else:
                    root.chars = prefix + random.choice(letters) + suffix
                return root
            left_size = random.randint(1, size-1)
            right_size = size - left_size
            if random.random() < 0.075:
                root.chars = prefix + f"[^{separator}]*" + suffix
                root.left = generate_tree(left_size)
                root.right = generate_tree(right_size)
            elif random.random() < 0.01:
                root.chars = prefix + f"{separator}?" + suffix
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

        for _ in range(numberOfRegexes):
            regex_tree = generate_tree(random.choice([5,10,15]))
            f.write(separator + traversal(regex_tree) + separator + "\n")

        f.close()

        print("Dataset " + str(dataset) + " generated.")
        dataset += 1
