#include <stdio.h>
#include <string.h>

int main(void) {
    char str[101];
    int a;
    scanf("%d", &a);
    for (int i = 0; i < a; i++) {
        scanf("%s", str);
        
        for (int j = 0; j < strlen(str); j++) {
            if (str[j] >= 'A' && str[j] <= 'Z') {
                str[j] += 32;
            }
        }
        
        printf("%s\n", str);
    }
    
    return 0;
}