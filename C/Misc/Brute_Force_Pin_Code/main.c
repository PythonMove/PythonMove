#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>


int pin_brute(char* input) {
    unsigned index = strlen(input) - 1;
    char *pin = calloc(index + 1, sizeof(char));
    memset(pin, '0', index + 1);

    while (1) {
        for (unsigned i = 0; i <= 9; i++) {
            if (strcmp(pin, input) == 0) {
                free(pin);
                return 0;
            }

            pin[index]++;
        }

        pin[index] = '9';
        for (unsigned j = index; j >= 0; j--) {
            if (pin[j] == '9') {
                pin[j] = '0';
                continue;
            }

            pin[j]++;
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
        total_time += ((double) (end - start)) / CLOCKS_PER_SEC;;
    }

    printf("Average execution time: %lfs", total / 10);
    return 0;
}
