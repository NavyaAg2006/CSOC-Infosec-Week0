#include<stdio.h>

void merge(double * arr,int low,int mid,int high)
{
    double temp[high-low+1];
    int g=0;
    int left=low,right=mid+1;
    while(left<=mid && right<=high)
        if(arr[left]<=arr[right])
            temp[g++]=arr[left++];
        else
            temp[g++]=arr[right++];
    while(right<=high)
        temp[g++]=arr[right++];
    while(left<=mid)
        temp[g++]=arr[left++];
    for(int x=low;x<=high;x++)
        arr[x]=temp[x-low];
}
void mergeSort(double* arr,int low , int high )
{
    if(low>=high)
        return;
    int mid=(low+high)/2;
    mergeSort(arr,low,mid);
    mergeSort(arr,mid+1,high);
    merge(arr,low,mid,high);
}

int main(void)
{
    int n;
    scanf("%d",&n);
    double a[n];
    for(int x=0;x<n;x++)
        scanf("%lf",&a[x]);
    mergeSort(a,0,n-1);
    for(int x=0;x<n;x++)
        printf("%lf ",a[x]);
    return 0;
}