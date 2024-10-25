#include <stdio.h>
#include <string.h>
int main(void) {
    int cnt = 0;
    char s[50001];
    fgets(s, sizeof(s), stdin);
    for (int i = 0; i < strlen(s); i++) {
        if (cnt == 10) {
            printf("\n");
            cnt = 0;
        }
        cnt++;
        printf("%c", s[i]);
    }
    return 0;
}