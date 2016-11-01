#include <iostream>
using namespace std;


bool binary_search(int arr[], int high, int low, int n) {
	int mid, beg = 0;
	int end = n + 1; // one position passed the right end
	while (beg < end) {
		mid = beg + (end - beg) / 2;
		if ((low > arr[mid]) && (high > arr[mid])) {
			beg = mid + 1;
		}
		else if ((low < arr[mid]) && (high < arr[mid])) {
			end = mid;
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
	int high = 14;
	int low = 10;

	int found = binary_search(arr, high, low, n);
        
        if (found == 1){
            cout << "True";
        }
        else if(found == 0){
            cout << "False";
        }

	return 0;
}
