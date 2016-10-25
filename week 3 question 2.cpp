code

#include<iostream>
using namespace std;

bool PrimeRec(int num, int divisor){
    
    if(divisor == 1){
        cout << num << " is a prime number" << endl;
        return true; 
        
    }
    if (num % divisor == 0){
        cout << num << " is not a prime number" << endl;
        return false;
    
    }
    else
        return PrimeRec(num, divisor - 1);
    
}



int main(){
    int num = 23;
    int divisor = num - 1;
    PrimeRec(num, divisor);
    return 0;
    
}
