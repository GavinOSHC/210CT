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
    
    int root = sqrt(n); 
    
    int floor_n = int(root);
    int ceil_n = floor_n + 1;    //Creat a ceil int
    
    
    // square both numbers 
    int floor_n_sqaure = floor_n * floor_n;
    int ceil_n_square = ceil_n * ceil_n; 
    
    // calculate square closest to the orginal
    int floor_gap = n - floor_n_sqaure;
    int ceil_gap = ceil_n_square - n;
    
    if (floor_gap < ceil_gap)
        cout << floor_n_sqaure;
        
    else 
        cout <<  ceil_n_square;
        
    
    
}


int main(){
    
    int n = 0;
    cout << "Please enter a number: " << endl;
    cin >> n; 
    HPS(n);
    return 0;
    
}
