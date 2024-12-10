# All Occurrences Pattern Searching

...

## Description

...

### Datasets

- Size of a pattern defined as a number of elements in the AST of the regex: `8, 16, 24, 32`.
- Size of the alphabet: `2, 8, 16, 24`.
- Size of an input text: `100000, 500000, 1000000`.

There are 48 datasets in total. Seeds are taken from random.org.


## Getting Started

### Requirements

-   Python.

### Installing

...

Generate the datasets with the following commands:
```
python generate.py 8 2 100000 7899802 > datasets\dataset01.txt
python generate.py 8 2 500000 7460683 > datasets\dataset02.txt
python generate.py 8 2 1000000 1338657 > datasets\dataset03.txt
python generate.py 8 8 100000 8442390 > datasets\dataset04.txt
python generate.py 8 8 500000 4933789 > datasets\dataset05.txt
python generate.py 8 8 1000000 7049795 > datasets\dataset06.txt
python generate.py 8 16 100000 4148354 > datasets\dataset07.txt
python generate.py 8 16 500000 8440021 > datasets\dataset08.txt
python generate.py 8 16 1000000 8645265 > datasets\dataset09.txt
python generate.py 8 24 100000 6863062 > datasets\dataset10.txt
python generate.py 8 24 500000 396043 > datasets\dataset11.txt
python generate.py 8 24 1000000 7535078 > datasets\dataset12.txt
python generate.py 16 2 100000 4250667 > datasets\dataset13.txt
python generate.py 16 2 500000 2444446 > datasets\dataset14.txt
python generate.py 16 2 1000000 3864871 > datasets\dataset15.txt
python generate.py 16 8 100000 8206617 > datasets\dataset16.txt
python generate.py 16 8 500000 3137384 > datasets\dataset17.txt
python generate.py 16 8 1000000 6065477 > datasets\dataset18.txt
python generate.py 16 16 100000 5554011 > datasets\dataset19.txt
python generate.py 16 16 500000 2593306 > datasets\dataset20.txt
python generate.py 16 16 1000000 1300077 > datasets\dataset21.txt
python generate.py 16 24 100000 4743383 > datasets\dataset22.txt
python generate.py 16 24 500000 4090998 > datasets\dataset23.txt
python generate.py 16 24 1000000 9549340 > datasets\dataset24.txt
python generate.py 24 2 100000 6389361 > datasets\dataset25.txt
python generate.py 24 2 500000 9467117 > datasets\dataset26.txt
python generate.py 24 2 1000000 3018315 > datasets\dataset27.txt
python generate.py 24 8 100000 8794870 > datasets\dataset28.txt
python generate.py 24 8 500000 737313 > datasets\dataset29.txt
python generate.py 24 8 1000000 1090698 > datasets\dataset30.txt
python generate.py 24 16 100000 7265486 > datasets\dataset31.txt
python generate.py 24 16 500000 5161077 > datasets\dataset32.txt
python generate.py 24 16 1000000 4121995 > datasets\dataset33.txt
python generate.py 24 24 100000 4542569 > datasets\dataset34.txt
python generate.py 24 24 500000 9490484 > datasets\dataset35.txt
python generate.py 24 24 1000000 2088170 > datasets\dataset36.txt
python generate.py 32 2 100000 2120306 > datasets\dataset37.txt
python generate.py 32 2 500000 6369361 > datasets\dataset38.txt
python generate.py 32 2 1000000 1164198 > datasets\dataset39.txt
python generate.py 32 8 100000 9505510 > datasets\dataset40.txt
python generate.py 32 8 500000 4925644 > datasets\dataset41.txt
python generate.py 32 8 1000000 5575150 > datasets\dataset42.txt
python generate.py 32 16 100000 9934394 > datasets\dataset43.txt
python generate.py 32 16 500000 3271666 > datasets\dataset44.txt
python generate.py 32 16 1000000 2197669 > datasets\dataset45.txt
python generate.py 32 24 100000 2875177 > datasets\dataset46.txt
python generate.py 32 24 500000 8840129 > datasets\dataset47.txt
python generate.py 32 24 1000000 2361737 > datasets\dataset48.txt
```

### Running

...

## Authors

Contributors names and contact info:

-   [Wojciech Wieczorek](https://kiia.ubb.edu.pl/pracownicy/dr-habwojciechwieczorek),
-   [Łukasz Strąk](https://ab.us.edu.pl/emp?id=47011),
-   [Arkadiusz Nowakowski](https://ab.us.edu.pl/emp?id=46971).
