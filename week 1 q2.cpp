#include <iostream>
using namespace std;


int findZeros(int n){
    //initialise the count 
    int count = 0;
    
    // setting error condition
    if (n < 0){
        cout << "No Factorial for a number less than 0" << endl;
    }
    
    if (n == 5)
        return 1;
        
   
    //diving n by 5
    while(n > 5){
        n = n/5;
        count = count + n; //count the number of loops
        
    }
    
    return count;
}

int main(){
    
    
    int n = 0;
    cout << "Please enter a positive number: ";
    cin >> n;
    cout << findZeros(n) << endl;
    
    return 0;
}

