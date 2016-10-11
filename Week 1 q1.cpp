#include <iostream>
#include <array>
#include <ctime>
#include <cstdlib>
using namespace std;

int shuffle(){
    
    //creating the array
    array<int, 8> newArray = {5,3,8,6,1,9,2,7};
    
    
    //seeding the random numbers
    srand(time(0));
    
    //looping thorugh the array 
    for(int x = 0; x < 8; x++){
        
        
        //generate a random number  
        int random = rand() % 8 + 0;
        
        //stop the repeating by switch newArray[x] with newArray[random]
        int rep = newArray[x];
        newArray[x] = newArray[random];
        newArray[random] = rep;
        
    }
    
    //looping thorugh the array printing out the values
    for (int x = 0; x < 8; x++){
        cout << newArray[x];
        
    }
    
}

int main(){
    
    shuffle();
    
    return 0; 
}
