using System.Collections.Immutable;
using Fare;

public class SuffixTree
{
  private static Queue<Place> _activePlaces = new();
  private static Automaton _automaton;
  private static string _text;
  public static int TextLength = -1;
  
  public class Node {
    public int begin;
    public int end;
    public int depth; // distance in characters from root to this node
    private ImmutableHashSet<int>? _suffixIndices;
    public Node parent;
    public Dictionary<char, Node> children;
    public Node suffixLink;

    public Node(int begin, int end, int depth, Node parent) {
      this.begin = begin;
      this.end = end;
      this.parent = parent;
      this.depth = depth;
      children = new();
      _suffixIndices = null;
    }

    private static void Traverse1(Node root)
    {
      Stack<Node> stack = new();
      stack.Push(root);
      Node? n;
      while (stack.TryPeek(out n))
      {
        if (n.children.Count == 0)
        {
          n._suffixIndices = ImmutableHashSet.Create<int>(TextLength - (n.depth + n.end - n.begin));
          stack.Pop();
        }
        else if (n.children.Any(p => p.Value._suffixIndices is not null))
        {
          IEnumerable<int> zb = n.children.SelectMany(p => p.Value._suffixIndices!);
          n._suffixIndices = zb.ToImmutableHashSet();
          stack.Pop();
        }
        else
        {
          foreach (Node child in n.children.Values)
          {
            stack.Push(child);
          }
        }
      }
    }

    public ImmutableHashSet<int> GetSuffixIndices()
    {
      if (_suffixIndices is null)
      {
        Traverse1(this);
      }
      return _suffixIndices!;
    }
  }

  public record struct Place(Node Vertex, int Offset, State CurrentState);
  
  public static Node buildSuffixTree(string s) {
    int n = s.Length;
    TextLength = n;
    Node root = new Node(0, 0, 0, null);
    Node node = root;
    for (int i = 0, tail = 0; i < n; i++, tail++) {
      Node last = null;
      while (tail >= 0) {
        Node ch; 
        while (node.children.TryGetValue(s[i - tail], out ch) && tail >= ch.end - ch.begin) {
          tail -= ch.end - ch.begin;
          node = ch;
        }
        if (ch == null) {
          node.children[s[i]] = new Node(i, n,
            node.depth + node.end - node.begin, node);
          if (last != null) last.suffixLink = node;
          last = null;
        } else {
          char t = s[ch.begin + tail];
          if (t == s[i]) {
            if (last != null) last.suffixLink = node;
            break;
          } else {
            Node splitNode = new Node(ch.begin, ch.begin + tail,
              node.depth + node.end - node.begin, node);
            splitNode.children[s[i]] = new Node(i, n, ch.depth + tail,
              splitNode);
            splitNode.children[t] = ch;
            ch.begin += tail;
            ch.depth += tail;
            ch.parent = splitNode;
            node.children[s[i - tail]] = splitNode;
            if (last != null) last.suffixLink = splitNode;
            last = splitNode;
          }
        }
        if (node == root) {
          --tail;
        } else {
          node = node.suffixLink;
        }
      }
    }
    return root;
  }

  private static void print(string s, int i, int j) {
    for (int k = i; k < j; k++)
      Console.Write(s[k]);
  }
  
  public static void printTree(Node n, string s, int spaces) {
    int i;
    for (i = 0; i < spaces; i++)
      Console.Write(" ");
    print(s, n.begin, n.end);
    Console.WriteLine($"{n.depth + n.end - n.begin} {n.GetHashCode()}");
    foreach (Node child in n.children.Values)
      printTree(child, s, spaces + 4);
  }
  
  private static void Traverse2(Node root)
  {
    Queue<Node> queue = new();
    queue.Enqueue(root);
    Node? n;
    while (queue.TryDequeue(out n))
    {
      Console.Write($"{n.GetHashCode()}:");
      foreach (int i in n.GetSuffixIndices())
      {
        Console.Write($" {i}");
      }
      Console.WriteLine();
      foreach (Node child in n.children.Values)
      {
        queue.Enqueue(child);
      }
    }
  }

  private static void performAlgorithm()
  {
    Place place;
    int counter = 0;
    while (_activePlaces.TryDequeue(out place))
    {
      if (place.CurrentState.Accept)
      {
        int j = place.Vertex.depth + place.Offset;
        foreach (int i in place.Vertex.GetSuffixIndices())
        {
          if (i < TextLength && i <= i + j - 1)
          {
            // Console.WriteLine($"{i}, {j}");
            ++counter;
          }
        }
      }
      if (place.Offset == place.Vertex.end - place.Vertex.begin)
      {
        foreach ((char c, Node nextVertex) in place.Vertex.children)
        {
          State? nextState = place.CurrentState.Step(c);
          if (nextState is not null)
          {
            _activePlaces.Enqueue(new Place(nextVertex, 1, nextState));
          }
        }
      }
      else
      {
        char c = _text[place.Vertex.begin + place.Offset];
        State? nextState = place.CurrentState.Step(c);
        if (nextState is not null)
        {
          _activePlaces.Enqueue(new Place(place.Vertex, place.Offset + 1, nextState));
        }
      }
    }
    Console.WriteLine($"{counter}");
  }
  
  public static void Main(string[] args)
  {
    string[] lines = File.ReadAllLines(args[0]);
    int n_regexes = lines.Length - 1;
    _text = lines[0].TrimEnd() + "$";
    // string text = "aabb$";
    Node root = buildSuffixTree(_text);
    // root.GetSuffixIndices();
    // printTree(root, text, 0);
    // Traverse1(root);
    // Traverse2(root);
    for (int iter = 1; iter <= n_regexes; ++iter)
    {
        _automaton = new RegExp(lines[iter].TrimEnd()).ToAutomaton();
        _activePlaces.Enqueue(new Place(root, 0, _automaton.Initial));
        performAlgorithm();
    }
  }
}
