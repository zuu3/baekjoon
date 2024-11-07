#include <stdio.h>
#include <string.h>

int main(void) {
    int a;
    char s[8];
    scanf("%d %s", &a, s);
    if (strcmp(s, "miss") == 0) printf("0");
    else if (strcmp(s, "bad") == 0) printf("%d", a * 200);
    else if (strcmp(s, "cool") == 0) printf("%d", a * 400);
    else if (strcmp(s, "great") == 0) printf("%d", a * 600);
    else if (strcmp(s, "perfect") == 0) printf("%d", a * 1000);
    return 0;
}