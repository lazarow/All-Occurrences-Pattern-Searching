using Fare;

static int Match(Automaton aut, ref string text, int idx, int max_length)
{
    int length = 0;
    int max_path = -1;
    State? state = aut.Initial;
    if (state.Accept) max_path = 0;
    while (length < max_length && (state = state!.Step(text[idx++])) is not null)
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
string pattern = data[1];

Automaton regex = new RegExp(pattern).ToAutomaton();

int textLength = text.Length;

for (int k = 0; k < textLength; k++) {
    int m = Match(regex, ref text, k, textLength - k);
    if (m > 0) {
        Console.WriteLine($"{k}, {k + m - 1}");
        for (int j = 1; j < m; j++) {
            int n = Match(regex, ref text, k, j);
            if (n == j) {
                Console.WriteLine($"{k}, {k + j - 1}");
            }
        }
    }
}
