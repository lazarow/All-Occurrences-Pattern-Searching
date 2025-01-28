# All Occurrences Pattern Searching

...

## Description

...

### Datasets

-   Size of a pattern defined as a number of elements in the AST of the regex: `16, 24, 32`.
-   Size of the alphabet: `4, 8, 16, 24`.
-   Size of an input text: `100000, 500000, 1000000`.

There are 36 datasets in total. Seeds are taken from random.org.

## Getting Started

### Requirements

-   Python.

### Installing

...

Generate the datasets with the following commands:

```
python generate.py 16 4 100000 4250679 > datasets/dataset01.txt
python generate.py 16 4 500000 2444451 > datasets/dataset02.txt
python generate.py 16 4 1000000 3864874 > datasets/dataset03.txt
python generate.py 16 8 100000 8206626 > datasets/dataset04.txt
python generate.py 16 8 500000 3137388 > datasets/dataset05.txt
python generate.py 16 8 1000000 6065478 > datasets/dataset06.txt
python generate.py 16 16 100000 5554015 > datasets/dataset07.txt
python generate.py 16 16 500000 2593314 > datasets/dataset08.txt
python generate.py 16 16 1000000 1300078 > datasets/dataset09.txt
python generate.py 16 24 100000 4743385 > datasets/dataset10.txt
python generate.py 16 24 500000 4090998 > datasets/dataset11.txt
python generate.py 16 24 1000000 9549340 > datasets/dataset12.txt
python generate.py 24 4 100000 6389365 > datasets/dataset13.txt
python generate.py 24 4 500000 9467124 > datasets/dataset14.txt
python generate.py 24 4 1000000 3018321 > datasets/dataset15.txt
python generate.py 24 8 100000 8794874 > datasets/dataset16.txt
python generate.py 24 8 500000 737313 > datasets/dataset17.txt
python generate.py 24 8 1000000 109081 > datasets/dataset18.txt
python generate.py 24 16 100000 7265492 > datasets/dataset19.txt
python generate.py 24 16 500000 5161081 > datasets/dataset20.txt
python generate.py 24 16 1000000 4122003 > datasets/dataset21.txt
python generate.py 24 24 100000 4542570 > datasets/dataset22.txt
python generate.py 24 24 500000 9490488 > datasets/dataset23.txt
python generate.py 24 24 1000000 2088170 > datasets/dataset24.txt
python generate.py 32 4 100000 2120307 > datasets/dataset25.txt
python generate.py 32 4 500000 6369363 > datasets/dataset26.txt
python generate.py 32 4 1000000 1164212 > datasets/dataset27.txt
python generate.py 32 8 100000 9505512 > datasets/dataset28.txt
python generate.py 32 8 500000 492567 > datasets/dataset29.txt
python generate.py 32 8 1000000 5575163 > datasets/dataset30.txt
python generate.py 32 16 100000 9934404 > datasets/dataset31.txt
python generate.py 32 16 500000 3271673 > datasets/dataset32.txt
python generate.py 32 16 1000000 2197673 > datasets/dataset33.txt
python generate.py 32 24 100000 2875185 > datasets/dataset34.txt
python generate.py 32 24 500000 8840130 > datasets/dataset35.txt
python generate.py 32 24 1000000 2361763 > datasets/dataset36.txt
```

### Running

...

## Authors

Contributors names and contact info:

-   [Wojciech Wieczorek](https://kiia.ubb.edu.pl/pracownicy/dr-habwojciechwieczorek),
-   [Łukasz Strąk](https://ab.us.edu.pl/emp?id=47011),
-   [Arkadiusz Nowakowski](https://ab.us.edu.pl/emp?id=46971).
