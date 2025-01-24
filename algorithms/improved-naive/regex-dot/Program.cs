using Fare;

int Match(Automaton aut, ref string text, int idx)
{
    int length = 0;
    int max_path = -1;
    State? state = aut.Initial;
    if (state.Accept) max_path = 0;
    while ((state = state!.Step(text[idx++])) is not null)
    {
        ++length;
        if (state.Accept) max_path = length;
    }
    return max_path;
}

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

//Regex primaryRegex = new Regex(primaryPattern, RegexOptions.Compiled);
//Regex secondaryRegex = new Regex(secondaryPattern, RegexOptions.Compiled);

Automaton primaryRegex = new RegExp(primaryPattern).ToAutomaton();
Automaton secondaryRegex = new RegExp(secondaryPattern).ToAutomaton();

primaryRegex.Run()

int textLength = text.Length;

for (int k = 0; k < textLength; k++) {
    var match = primaryRegex.Match(text, k);
    if (match.Success && match.Length > 0 && match.Index == k) {
        int m = match.Length;
        Console.WriteLine($"{k}, {k + m - 1}");
        for (int j = 1; j < m; j++) {
            var secondaryMatch = secondaryRegex.Match(text.Substring(k, j));
            if (secondaryMatch.Success) {
                Console.WriteLine($"{k}, {k + j - 1}");
            }
        }
    }
}
