#include <iostream>
using namespace std;


void insertionSort(int arr[], int size){
    
    int j, temp;
    
    for(int i = 1; i < size; i++){
        j = i;
        
        while(j > 0 && arr[j - 1] > arr[j]){
            temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j--;
        }
        
    }
}


int main(){
    
    
    int arr[] = {5,6,3,7,9,1};
    int size = 6;
    
    insertionSort(arr, size);
    
    for(int i = 0; i < size; i++){
        
        cout<<arr[i];
    }

}
