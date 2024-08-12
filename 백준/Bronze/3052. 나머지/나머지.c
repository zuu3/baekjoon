#include <stdio.h>
#include <stdbool.h>

int main(void) {
    bool arr[42] = {false};
    int num;
    
    for (int i = 0; i < 10; i++) {
        scanf("%d", &num);
        int chk = num % 42;
        arr[chk] = true;
    }
    
    int cnt = 0;
    for (int i = 0; i < 42; i++) {
        if (arr[i]) {
            cnt++;
        }
    }
    
    printf("%d\n", cnt);
    
    return 0;
}