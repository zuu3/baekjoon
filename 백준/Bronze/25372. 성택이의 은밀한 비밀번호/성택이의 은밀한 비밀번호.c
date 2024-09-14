#include <stdio.h>
#include <string.h>
int main(void) {
    int a;
    char str[21];
    scanf("%d", &a);
    for (int i = 0; i < a; i++) {
        scanf("%s", str);
        if (strlen(str) >= 6 && strlen(str) <= 9) printf("yes\n");
        else printf("no\n");
    }
    return 0;
}