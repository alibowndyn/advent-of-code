import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Part1_2 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("../input.txt"));
        List<Integer> group1 = new ArrayList<>();
        List<Integer> group2 = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("   ");

            group1.add( Integer.parseInt(parts[0]) );
            group2.add( Integer.parseInt(parts[1]) );
        }

        part1(group1, group2);
        part2(group1, group2);
    }

    private static void part1(List<Integer> group1, List<Integer> group2) {
        Collections.sort(group1);
        Collections.sort(group2);

        int total_distance = 0;

        for (int i = 0; i < group1.size(); i++)
            total_distance += Math.abs( group1.get(i) - group2.get(i) );

        System.out.println(total_distance);
    }

    private static void part2(List<Integer> group1, List<Integer> group2) {
        int similarity_score = 0;
        int count = 0;

        for (int id_to_count : group1) {
            count = 0;

            for (int id : group2) {
                if (id == id_to_count)
                    count++;
            }

            similarity_score += id_to_count * count;
        }

        System.out.println(similarity_score);
    }
}