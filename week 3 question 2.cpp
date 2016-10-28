psuedocode

num <- enter number
div <- num - 1

ISPRIME(num,div):
    if div equal to 1:
        return true
    
    if num % div equal to 1:
         return false
    
    else:
        return ISPRIME(num div - 1)
            


code

#include<iostream>
using namespace std;

bool PrimeRec(int num, int divisor){
    
    if(divisor == 1){                                   //if the divisor is equal to 1 that means the number must be a prime
        cout << num << " is a prime number" << endl;        
        return true; 
        
    }
    if (num % divisor == 0){                            //if there is no remainder when dividing num and the divisor it must not be a prime 
        cout << num << " is not a prime number" << endl;
        return false;
    
    }
    else
        return PrimeRec(num, divisor - 1);             //run recursion by -1 the divisor untill one of the other if statements are true
    
}



int main(){
    int num = 23;                      
    int divisor = num - 1;            //divisor has to start with the one less than the number
    PrimeRec(num, divisor);
    return 0;
    
}



//the  bigO notation for this algorithm is o(n) as the algorithm will only run n number of time until div is equal to 1 
//or the other if statement are ment. 
