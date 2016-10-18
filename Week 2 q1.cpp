pseudocode

HPS(n):
  root <- sqrt(n)    // Root the number given 
  
  floor_n <- int(root)   // Round root to a int 
  ceil_n <- floor_n + 1  // Create ceil int
  
  // Square both integers
  floor_n_square <- floor_n * floor_n
  ceil_n_square <- ceil_n * ceil_n
  
  // Calcute sqaure closest to the original
  floor_gap <- n - floor_n_square
  ceil_gap <- ceil_n_square - n
  if floor_gap < ceil_gap then
    print floor_n_squard
  else 
    print ceil_n_squard
  
  
Code in C++

#include<iostream>
#include<math.h>
using namespace std;


int HPS(int n){
     
    for(int i = 1; i < n; i++){     // start the loop 
        if(i*i > n){                // if i is greater then than number,  
            n = (i-1) * (i-1);     
            break;
        }
    
        if (i*i == n)           // if i squard is equal to n return i squard
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
