#include <iostream>
using namespace std;


bool binary_search(int arr[], int high, int low, int n) {
	int mid, beg = 0;					// set the varible mid to 0 and the begining to 0
	int end = n;						// set end equal to the array size
	while (beg < end) {					
		mid = beg + (end - beg) / 2;			// get the middle index value of the array 
		if ((low > arr[mid]) && (high > arr[mid])) {	// check if low and high are greater than middle value 
			beg = mid + 1;				// add one to mid and it now becomes the middle
		}
		else if ((low < arr[mid]) && (high < arr[mid])) {	// check if low and high are lower than middle value
			end = mid;					// if it is true the end of the array is the mid
		}
		else {
			return true;
		}
	}

	return false;
}


int main() {
	int n = 6;
	int arr[25] = { 2,3,5,7,9,13 };
	int high = 22;
	int low = 21;

	int found = binary_search(arr, high, low, n);
        
	// use the return values of the function to ouput true or false instead of 1 or 0
        if (found == 1){			
            cout << "True";
        }
        else if(found == 0){
            cout << "False";
        }
	
	return 0;
}

// The big O noation for this algorithm is O(Log N) as it splits the array in half and keeps doing it until the answer is found. 
