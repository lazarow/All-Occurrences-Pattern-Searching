using System.Text.RegularExpressions;

if (args.Length == 0)
{
    Console.WriteLine("Please provide a file name as the first argument.");
    return;
}

// Read the file name from the command line.
string fileName = args[0];

// Read the file.
string[] data = File.ReadAllLines(fileName);

// Get the text and regular expression from the file.
string text = data[0];
string primaryPattern = data[1];
string secondaryPattern = primaryPattern.StartsWith("^") ? primaryPattern : "^" + primaryPattern;
secondaryPattern = secondaryPattern.EndsWith("$") ? secondaryPattern : secondaryPattern + "$";

Regex primaryRegex = new Regex(primaryPattern, RegexOptions.Compiled);
Regex secondaryRegex = new Regex(secondaryPattern, RegexOptions.Compiled);

int textLength = text.Length;

for (int k = 0; k < textLength; k++) {
    var match = primaryRegex.Match(text, k);
    if (match.Success && match.Index == k) {
        int m = match.Length;
        Console.WriteLine($"{k}, {m}");
        for (int j = 1; j < m; j++) {
            var secondaryMatch = secondaryRegex.Match(text, k, j);
            if (secondaryMatch.Success) {
                Console.WriteLine($"{k}, {j}");
            }
        }
    }
}
