
string[] lines = File.ReadAllLines("../input.txt");

List<int> group1 = [];
List<int> group2 = [];

foreach (string line in lines)
{
    string[] parts = line.Split("   ");

    group1.Add( int.Parse(parts[0]) );
    group2.Add( int.Parse(parts[1]) );
}

Part1(group1, group2);
Part2(group1, group2);


static void Part1(List<int> group1, List<int> group2)
{
    group1.Sort();
    group2.Sort();

    int total_distance = 0;
    foreach ((int id_1, int id_2) in group1.Zip(group2))
    {
        total_distance += Math.Abs(id_1 - id_2);
    }

    Console.WriteLine(total_distance);
}

static void Part2(List<int> group1, List<int> group2)
{
    int similarity_score = 0;
    int count;

    foreach (int id_to_count in group1)
    {
        count = 0;
        foreach (int id in group2)
        {
            if (id == id_to_count)
                count++;
        }

        similarity_score += id_to_count * count;
    }

    Console.WriteLine(similarity_score);
}