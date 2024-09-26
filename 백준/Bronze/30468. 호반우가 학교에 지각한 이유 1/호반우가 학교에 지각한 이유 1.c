#include <stdio.h>

int main(void) {
    int STR, DEX, INT, LUK, N;
    scanf("%d %d %d %d %d", &STR, &DEX, &INT, &LUK, &N);
    double avg = (STR + DEX + INT + LUK) / 4.0;

    if (N > avg) printf("%d", (int)((N - avg) * 4));
    else printf("0");

    return 0;
}