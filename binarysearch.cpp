#include <iostream>
using namespace std;

bool binarysearch(int arr[], int size, int key){
  int start = 0;
  int mid = 0
  int end = size;
  
  while(start < end){
    mid = start + (start + end) / 2;
    if(key > mid){
      start = mid + 1;
    }
    else if(key < mid){
      end = mid
    }
    else
      return true;
  }
  
 return false; 
}


int main(){
  int arr[] = {1,2,3,4,5,6};
  int size = 6;
  int key = 5;
}
