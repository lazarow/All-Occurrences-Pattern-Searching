using Fare;

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

    int length = 0;
    int max_length = textLength - k;
    State? state = regex.Initial;
    while (length < max_length && (state = state!.Step(text[k + length++])) is not null)
    {
        if (state.Accept) {
            Console.WriteLine($"{k}, {length}");
        }
    }
}
