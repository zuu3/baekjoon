#include <stdio.h>

void bubble_sort(int list[], int n){
  int temp;

  for(int i = n-1; i>0; i--){
    for(int j = 0; j<i; j++){
      if(list[j]>list[j+1]){
        temp = list[j];
        list[j] = list[j+1];
        list[j+1] = temp;
      }
    }
  }
}

int main(void) {
    int a;
    scanf("%d", &a);
    int arr[a];
    for (int i = 0; i < a; i++) {
        scanf("%d", &arr[i]);
    }
    bubble_sort(arr, a);
    for (int i = 0; i < a; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}