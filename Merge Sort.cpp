#include <iostream>
using namespace std;


void merge(int arr[], int size, int low, int middle, int high){
    int temp[size];
    
    for(int i = low; i <= high; i++){
        temp[i] = arr[i];
    }
    
    
    int i = low;
    int j = middle+1;
    int k = low;
    
    while( i <= middle && j <= high){
        if(temp[i] < temp[j]){
            arr[k] = temp[i];
            i++;
        }
        
        else{
            arr[k] = temp[j];
            j++;
        }
        k++;
    }
    
    while(i <= middle){
        arr[k] = temp[i];
        i++;
        k++;
    }
    
}

void mergeSort(int arr[], int size, int low, int high){
    if(low < high){
        int middle = (low + high) / 2;
        mergeSort(arr, size, low, middle);
        mergeSort(arr, size, middle+1, high);
        merge(arr, size, low, middle, high);
    }
}


int main(){
    
    
    int arr[] = {5,6,3,7,9,1};
    int size = 6;
    
    mergeSort(arr, size, 0, 5);
    
    for(int i = 0; i < size; i++){
        
        cout<<arr[i];
    }

}