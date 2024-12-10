using System;
using System.Text.RegularExpressions;
using System.Collections;

var resultSet = new HashSet<string>();

string[] data = File.ReadAllLines("text.txt");

string text = data[0];
string pattern = data[1];

Console.WriteLine($"Finding all patterns: {pattern} for the text.");

void PrintIfFound(Match match, int start) {
    var end = match.Index + match.Length;    
    resultSet.Add($"{start+match.Index}:{start+end} {match.Captures[0].Value}"); 
    Console.WriteLine($"{start+match.Index}, {start+end}");
}

// int op = 0;

// void FindIter(int start, int length) {
//     op++;
//     if (start + length > text.Length)
//         return;
    
//     var match = Regex.Match(text.Substring(start, length), pattern);

//     if (match.Success) {
//         PrintIfFound(match, start);
//         int newStart = start + match.Index;        
//         FindIter(newStart, match.Length-1);
//         FindIter(newStart+1, match.Length-1);
//     }
// }

// FindIter(0, text.Length);

// //Console.Write(string.Join("\n", resultSet));

// Console.WriteLine();

// Console.WriteLine($"Number of operations: {op}");

// Console.WriteLine($"Size of set: {resultSet.Count}");

// op = 0;
// resultSet.Clear();

// for (int i=0; i<text.Length-1; i++)
//     for (int j=text.Length; j>i; j--){
//        op++; 
//        var match = Regex.Match(text.Substring(i, j-i), pattern);

//         if (match.Success) {
//             PrintIfFound(match, i);            
//         }
//     }

// //Console.Write(string.Join("\n", resultSet)); 

// Console.WriteLine();

// Console.WriteLine($"Naive method operations: {op}");

// Console.WriteLine($"Size of set: {resultSet.Count}");

int op = 0;
resultSet.Clear();

Regex regex = new Regex(pattern, RegexOptions.Compiled);

for (int i=0; i < text.Length-1; i++)
    for (int j=text.Length; j>i;){
       op++; 
       var match = regex.Match(text.Substring(i, j-i));

        if (match.Success) {
            PrintIfFound(match, i);            
            i = i + match.Index;
            j = i + match.Length -1;            
        }
        else
            break;        
    }

//Console.Write(string.Join("\n", resultSet)); 

Console.WriteLine();

Console.WriteLine($"Inproved method operations: {op}");

Console.WriteLine($"Size of set: {resultSet.Count}");