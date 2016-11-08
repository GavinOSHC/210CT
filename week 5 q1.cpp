#include<iostream>
#include<math.h>
using namespace std;

int sub(int arr[]){
    
    int subSeqLength = 1;
    int longest = 1;
    int indexStart = 0;
    int indexEnd = 0;
    int r = sizeof(arr) / sizeof (arr[0]); //getting the length of the array
    
    
    for(int i = 0; i < r + 1; i++){
        if(arr[i] == arr[i]){
            subSeqLength++;
            
            if(subSeqLength > longest){
                longest = subSeqLength;
                indexStart = i + 2 - subSeqLength;
                indexEnd = i + 2;
                
            }
        }
        
        else{
            subSeqLength = 1;
            
        }
        
    }
    
    for(int i = indexStart; i < indexEnd; i++){
        cout << arr[i];
    }
    
    
    
    
}


int main(){
    
    int arr[] = {1,2,3,4,1,5,1,6,7};
    
    sub(arr);

    return 0;
}
