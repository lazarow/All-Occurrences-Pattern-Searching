import sys
import random

sizeOfPattern = int(sys.argv[1])
sizeOfAlphabet = int(sys.argv[2])
sizeOfText = int(sys.argv[3])
seed = int(sys.argv[4])

random.seed(seed)

TERMINALS = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]
OPERATORS = ['*', '', '|']

print(''.join(random.choices(TERMINALS, k=sizeOfText)))
