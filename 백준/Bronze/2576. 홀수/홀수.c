#include <stdio.h>

int main(void) {
    int arr[8];
    int oddarr[8] = {0};
    int min = 101;
    int hap = 0;
    for (int i = 0; i < 7; i++) {
        scanf("%d", &arr[i]);
        if (arr[i]%2) oddarr[i] = arr[i];
        if (oddarr[i] < min && oddarr[i] != 0) min = oddarr[i];
        hap += oddarr[i];
    }
    if (hap) printf("%d\n%d", hap, min);
    else printf("-1");
    return 0;
}