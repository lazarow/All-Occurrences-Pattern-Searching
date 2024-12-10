import sys
import random

sizeOfPattern = int(sys.argv[1])
sizeOfAlphabet = int(sys.argv[2])
sizeOfText = int(sys.argv[3])
seed = int(sys.argv[4])

random.seed(seed)

TERMINALS = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]
OPERATORS = ['*', '', '|']

def gen(size, starparent=False):
    if size <= 1:
        return random.choice(TERMINALS)
    else:
        if starparent:
            op = random.choice(OPERATORS[1:])
        else:
            op = random.choice(OPERATORS)
        if op == '*':
            return '(' + gen(size - 1, True) + '*)'
        size -= 1
        r = random.randint(1, max(1, size - 1))
        return '(' + gen(r) + op + gen(size - r) + ')'

print(''.join(random.choices(TERMINALS, k=sizeOfText)))
print(gen(sizeOfPattern))
