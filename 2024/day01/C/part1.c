#include <stdio.h>
#include <stdlib.h>



int cmp_int(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main()
{
    char line_buf[15];
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

    qsort(group1, line_cnt, sizeof(int), cmp_int);
    qsort(group2, line_cnt, sizeof(int), cmp_int);


    int total_distance = 0;
    for (int i = 0; i < line_cnt; i++)
        total_distance += abs(group1[i] - group2[i]);

    printf("%d\n", total_distance);


    free(group1);
    free(group2);

    return EXIT_SUCCESS;
}