#include <stdio.h>

int main(void) {
    int a;
    scanf("%d", &a);
    for (int i = 0; i < a; i++) {
        int n1,n2;
        scanf("%d,%d", &n1, &n2);
        printf("%d\n", n1+n2);
    }
    return 0;
}