#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int main()
{
    FILE* input = fopen("../input.txt", "r");

    char num_buf[3] = {'\0'};
    int calib_sum = 0;

    char is_first_in_line = 0;
    char last_digit_in_line;
    char chr;


    while ( (chr = fgetc(input)) != EOF)
    {
        if (isdigit(chr))
        {
            last_digit_in_line = chr;

            if (!is_first_in_line)
            {
                num_buf[0] = last_digit_in_line;
                is_first_in_line = 1;
            }
        }
        else if (chr == '\n')
        {
            num_buf[1] = last_digit_in_line;
            calib_sum += atoi(num_buf);

            num_buf[0] = '\0';
            is_first_in_line = 0;
        }
    }


    printf("%d", calib_sum);


    fclose(input);
    return EXIT_SUCCESS;
}