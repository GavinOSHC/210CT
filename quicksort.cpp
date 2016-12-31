#include <iostream>
using namespace std;



void quick(int arr[], int left, int right){
	int i = left;
	int j = right;
	int temp;
	int pivot = arr[(left + right)/2];
	
	while(i <= j){
		while(arr[i] < pivot){
			i++;
		}
		
		while(arr[j] > pivot){
			j--;
		}
		if(i <= j ){
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j++;
		}
		
	}
	
	if(left < j)
		quick(arr, left, j);
		
	if(i < right)
		quick(arr,i, right);

}



int main() {
	int arr_size = 6;
	int arr[] = {1,5,9,8,4,7};

	
	quick(arr, 0, arr_size - 1);
	
	for(int i = 0; i < arr_size; i++){
		cout << arr[i] << " ";
	}
	
	return 0;	
}
