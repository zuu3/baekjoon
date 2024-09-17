#include <stdio.h>

int factorial(int a) {
    int result = 1;
    for (int i = 1; i <= a; i++) {
        result *= i;
    }
    return result;
}

int main(void) {
    int N, K;
    scanf("%d %d", &N, &K);
    printf("%d", factorial(N) / (factorial(K) * factorial(N - K)));
    return 0;
}