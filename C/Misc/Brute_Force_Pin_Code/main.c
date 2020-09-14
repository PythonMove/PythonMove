#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>


int pin_brute(char* pin_code) {
    unsigned last_index = strlen(pin_code) - 1;
    char *attempt = calloc(last_index + 1, sizeof(char));
    memset(attempt, '0', last_index + 1);

    while (1) {
        for (unsigned i = 0; i <= 9; i++) {
            if (strcmp(attempt, pin_code) == 0) {
                free(attempt);
                return 0;
            }

            attempt[last_index]++;
        }

        attempt[last_index] = '9';
        for (unsigned j = last_index; j >= 0; j--) {
            if (attempt[j] == '9') {
                attempt[j] = '0';
                continue;
            }

            attempt[j]++;
            break;
        }
    }
}


int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Missing PIN code as an argument!");
        return 1;
    }

    printf("PIN code: %s\n", argv[1]);

    double total_time = 0;
    for (int k = 0; k < 10; k++) {
        clock_t start_time = clock();
        pin_brute(argv[1]);
        clock_t end_time = clock();
        total_time += ((double) (end_time - start_time)) / CLOCKS_PER_SEC;;
    }

    printf("Average execution time: %.3lfs\n", total_time / 10);
    return 0;
}
