pseudocode

HPS(n):
  for i <- 1; i is less than n; i++:
      if i times i is greater than n:
        n <- i minus 1 times i minus 1
          break 
          
      if i times i is eqaul to n:
            return i times i 
            
  
  return n 
    
Code in C++

#include<iostream>
#include<math.h>
using namespace std;


int HPS(int n){
     
    for(int i = 1; i < n; i++){     // start the loop with i untill it equal the square number of n
        if(i*i > n){            
            n = (i-1) * (i-1);      // to find the lowest perfect square of n 
            break;
        }
    
        if (i*i == n)           // if i squared is equal to n return i
            return(i*i);
    }
    
    return n;
    

}


int main(){
    
    int n = 0;
    cout << "Please enter a number: " << endl;
    cin >> n; 
    cout << HPS(n);
    return 0;
    
}
