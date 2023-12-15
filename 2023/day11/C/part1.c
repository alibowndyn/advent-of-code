#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    FILE* input = fopen("../input.txt", "r");

    int row_len = 0;
    while ( getc(input) != '\n' )
        row_len++;

    char line[row_len + 2]; // +2 for '\n' and '\0'
    char blank_row[row_len];

    // make a blank row
    memset(blank_row, '.', row_len);
    blank_row[row_len] = '\0';

    int blank_row_indices[row_len];
    int blank_col_indices[row_len];
    int num_blank_rows = 0;
    int num_blank_cols = 0;

    int galaxies = 0;


    // get the index of every blank row
    for (int i = 0; fgets(line, sizeof(line), input) != NULL; i++)
    {
        line[row_len] = '\0';
        if (strcmp(line, blank_row) == 0)
        {
            blank_row_indices[num_blank_rows++] = i;
        }
    }
    rewind(input);


    // get the index of every blank column
    int is_col_blank = 1;
    for (int i = 0; i < row_len; i++)
    {
        is_col_blank = 1;
        while (fgets(line, sizeof(line), input) != NULL)
        {
            if (line[i] == '#')
            {
                is_col_blank = 0;
                galaxies++;
            }
        }

        rewind(input);

        if (!is_col_blank)
            continue;
        else
            blank_col_indices[num_blank_cols++] = i;
    }


    int y_coords[galaxies];
    int x_coords[galaxies];
    int cnt_y = 0, cnt_x = 0;
    int j = 0;

    // For every galaxy, we will offset that galaxy's (y, x) coordinate with the
    // number of blank rows & columns before it, times the expansion rate.
    for (int y = 0; fgets(line, sizeof(line), input) != NULL; y++)
    for (int x = 0; x < row_len; x++)
    {
        if (line[x] == '#')
        {
            cnt_y = cnt_x = 0;

            // count the number of blank rows before this galaxy
            for (int i = 0; i < num_blank_rows; i++)
            {
                if (y > blank_row_indices[i])
                    cnt_y++;
            }

            // count the number of blank columns before this galaxy
            for (int i = 0; i < num_blank_cols; i++)
            {
                if (x > blank_col_indices[i])
                    cnt_x++;
            }

            // coords after the expansion
            y_coords[j  ] = y + cnt_y;
            x_coords[j++] = x + cnt_x;
        }
    }



    fclose(input);
    long sum = 0;

    // for every galaxy pair, calculate the shortest path between them
    for (    j =   0; j < galaxies; j++)
    for (int k = j+1; k < galaxies; k++)
    {
        // |y2 - y1| + |x2 - x1|
        sum += abs(y_coords[k] - y_coords[j]) + abs(x_coords[k] - x_coords[j]);
    }


    printf("%ld\n", sum);

    return EXIT_SUCCESS;
}