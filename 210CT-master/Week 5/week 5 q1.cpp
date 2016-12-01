#include<iostream>
#include<math.h>
using namespace std;

int sub(int arr[], int sizeArr){
    
    int subSeqLength = 1;
    int longest = 1;
    int indexStart = 0;
    int indexEnd = 0;
    
    
    
    for(int i = 0; i < sizeArr + 1; i++){
        if(arr[i] == arr[i + 1] - 1){           //Check if the current value is equal 
            subSeqLength++;             // if it is increment 
            
            
            
            if(subSeqLength > longest){  //Setting the subSeqLength to a value longest
                longest = subSeqLength;
                indexStart = i + 2 - subSeqLength;  // Making sure that the index start is correct
                indexEnd = i + 2;
                
            }
        }
        
        else{
            subSeqLength = 1;       //if its no longer increasing set the value to 1
            
        }
        
    }
    
    for(int i = indexStart; i < indexEnd; i++){     // printing out the numbers
        cout << arr[i] << ",";
    }
    
    
    
    
}


int main(){
    
    int arr[] = {1,3,3,4,1,2,3,4,7};
    int sizeArr = sizeof(arr) / sizeof (arr[0]); //getting the length of the array
    
    sub(arr,sizeArr);

    return 0;
}
