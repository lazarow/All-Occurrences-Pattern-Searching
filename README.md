# All Occurrences Pattern Searching

## Description

This project implements and compares two algorithms for finding all occurrences including overlaps of regular expression patterns in text:

1. an efficient algorithm using suffix trees and automata,
2. an improved naive approach using direct pattern matching.

### Datasets

-   Size of a pattern defined as a number of elements in the AST of the regex: `50, 100, 200`.
-   Size of the alphabet: `4, 8, 16, 24`.
-   Size of an input text: `500000, 1000000, 2000000`.

There are 36 datasets in total.

A dataset file consists:

-   an input text in the first line,
-   a pattern (regular expression) in the second line.

Example:

```
cbbdacbcacbabaadbdbdbaacbdcbccabbacacdcbcababdcabcbbcdcbbcaacbacdcbbbdddddcccada
bd.*bdd(d|bbd.*d)abc(d|a)a
```

## Getting Started

### Requirements

-   Python.
-   .NET 8.

### Installing

Generate the predefined datasets with the following commands:

```
python generate.py
```

Compile the algorithms with the following commands:

```
cd algorithms/automaton-on-suffix-tree/
dotnet build -c=Release
cd algorithms/improved-naive/
dotnet build -c=Release
```

### Running

Run all datasets with the following command:

```
chmod +x runner.sh
./runner.sh > out.log 2>&1
```

Run a single dataset with the following command:

```
algorithms/automaton-on-suffix-tree/STzad11/bin/Release/net8.0/STzad11 <dataset-path>
algorithms/improved-naive/regex-dot/bin/Release/net8.0/regex-dot <dataset-path>
```

## Authors

Contributors names and contact info:

-   [Wojciech Wieczorek](https://kiia.ubb.edu.pl/pracownicy/dr-habwojciechwieczorek),
-   [Łukasz Strąk](https://ab.us.edu.pl/emp?id=47011),
-   [Arkadiusz Nowakowski](https://ab.us.edu.pl/emp?id=46971).
