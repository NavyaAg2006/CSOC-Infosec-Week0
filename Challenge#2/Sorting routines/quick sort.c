#include <stdio.h>

void swap(double* a, double* b) {
    double t = *a;
    *a = *b;
    *b = t;
}

int pivot(double* a, int low, int high) {
    int i = low, j = high - 1;
    double k = a[high];
    while (i <= j) {
        while (i <= high && a[i] <= k)
            i++;
        while (j >= low && a[j] > k)
            j--;
        if (i < j)
            swap(&a[i], &a[j]);
    }
    swap(&a[i], &a[high]);
    return i;
}

void quicksort(double* a, int low, int high) {
    if (low < high) {
        int pi = pivot(a, low, high);
        quicksort(a, low, pi - 1);
        quicksort(a, pi + 1, high);
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    double a[n];
    for (int x = 0; x < n; x++)
        scanf("%lf", &a[x]);
    quicksort(a, 0, n - 1);
    for (int x = 0; x < n; x++)
        printf("%lf ", a[x]);
    return 0;
}