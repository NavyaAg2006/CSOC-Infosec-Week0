#include <stdio.h>

void insertMaxHeap(int arr[], int *n, int value) {
    (*n)++;
    int i = *n;
    arr[i] = value;

    while (i > 1 && arr[i] > arr[i / 2]) {
        int temp = arr[i];
        arr[i] = arr[i / 2];
        arr[i / 2] = temp;
        i = i / 2;
    }
}

int deleteMaxHeap(int arr[], int *n) {
    if (*n == 0) return -1;

    int maxVal = arr[1];
    arr[1] = arr[*n];
    (*n)--;

    int i = 1, left, right, largest;
    while (1) {
        left = 2 * i;
        right = 2 * i + 1;
        largest = i;

        if (left <= *n && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right <= *n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest == i) break;

        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        i = largest;
    }
    return maxVal;
}

void heapSort(int arr[], int size) {
    int heap[size + 1];
    int heapSize = 0;

    for (int i = 0; i < size; i++) {
        insertMaxHeap(heap, &heapSize, arr[i]);
    }

    for (int i = size - 1; i >= 0; i--) {
        arr[i] = deleteMaxHeap(heap, &heapSize);
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter array elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Original array: \n");
    printArray(arr, n);

    heapSort(arr, n);

    printf("Sorted array: \n");
    printArray(arr, n);

    return 0;
}
