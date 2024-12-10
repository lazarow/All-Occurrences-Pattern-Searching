using System.Diagnostics;
using System.Text.RegularExpressions;

string defaultFileName = "/Users/lukaszstrak/Repo/All-Occurrences-Pattern-Searching/datasets/dataset01.txt";

string fileName = args.Length == 2 ? args[0] : defaultFileName;

bool runImproved = true;

if (args.Length == 2)
    runImproved = args[1] == "2";

var resultSet = new HashSet<string>();

string[] data = File.ReadAllLines(fileName);

string text = data[0];
string pattern = data[1];

Console.WriteLine($"Finding all patterns: {pattern} for the text.");

void PrintIfFound(Match match, int start) {
    if(string.IsNullOrEmpty(match.Captures[0].Value))
        return;
    var end = match.Index + match.Length;    
    bool added = resultSet.Add($"{start+match.Index}:{start+end} {match.Captures[0].Value}"); 
    if (added)
        Console.WriteLine($"{start+match.Index}, {start+end} {match.Captures[0].Value}");
}

int op = 0;

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

if(!runImproved) {
    op = 0;
    resultSet.Clear();

    Regex regex = new Regex(pattern, RegexOptions.Compiled);

    for (int i=0; i<text.Length-1; i++)
        for (int j=text.Length; j>i; j--){
        op++; 
        var match = regex.Match(text.Substring(i, j-i));

        if (match.Success) {
            PrintIfFound(match, i);            
        }
        }

    //Console.Write(string.Join("\n", resultSet));

    Console.WriteLine();

    Console.WriteLine($"Naive method operations: {op}");

    Console.WriteLine($"Size of set: {resultSet.Count}");
}
else {
    op = 0;
    resultSet.Clear();

    Regex regex = new Regex(pattern, RegexOptions.Compiled);

    for (int i=0; i < text.Length-1; i++)
        for (int j=text.Length; j>i;) {
            op++; 
            var match = regex.Match(text.Substring(i, j-i));

            if (match.Success) {
                PrintIfFound(match, i);                
                j = i + match.Length -1;            
            }
            else
                break;        
        }

    //Console.Write(string.Join("\n", resultSet)); 

    Console.WriteLine();

    Console.WriteLine($"Improved method operations: {op}");

    Console.WriteLine($"Size of set: {resultSet.Count}");
}