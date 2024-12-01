#include <stdio.h>
#include <stdlib.h>



int main()
{
    char line_buf[15]; // 10 digits + 3 spaces + 1 newline + 1 null terminator
    FILE *fp = fopen("../input.txt", "r");

    int line_cnt = 0;
    while ( fgets(line_buf, sizeof(line_buf), fp) != NULL )
        line_cnt++;

    size_t group_size = line_cnt * sizeof(int);
    int *group1 = malloc(group_size);
    int *group2 = malloc(group_size);


    rewind(fp);
    for (int i = 0; i < line_cnt; i++)
    {
        fgets(line_buf, sizeof(line_buf), fp);

        // atoi reads a string until there are no convertible characters left
        // and since spaces (and newlines) cannot be converted to numbers,
        // it will stop at those points in the string
        group1[i] = atoi(line_buf);
        group2[i] = atoi(line_buf + 8); // the second number starts at the 9th character in a line
    }


    int similarity_score = 0;
    int count;

    for (int i = 0; i < line_cnt; i++)
    {
        count = 0;
        for (int j = 0; j < line_cnt; j++)
        {
            if (group2[j] == group1[i])
                count++;
        }

        similarity_score += group1[i] * count;
    }

    printf("%d\n", similarity_score);


    free(group1);
    free(group2);

    return EXIT_SUCCESS;
}
