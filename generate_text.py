import sys
import random

sizeOfAlphabet = int(sys.argv[1])
sizeOfText = int(sys.argv[2])
seed = int(sys.argv[3])

random.seed(seed)

TERMINALS = [chr(ord('a') + i) for i in range(sizeOfAlphabet)]

print(''.join(random.choices(TERMINALS, k=sizeOfText)))
