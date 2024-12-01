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
        // `fscanf` skips whitespaces
        fscanf(fp, "%d %d", &group1[i], &group2[i]);


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
