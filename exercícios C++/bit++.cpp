#include <iostream>
using namespace std;

int main(){

    string statement; 
    int n, x=0;
    cin>>n;
    
    for(int i = n; i > 0; i--){
        cin>>statement;
        if(statement == "X++" || statement == "++X"){ x++; }
        else if(statement == "X--" || statement == "--X"){ x--; }
    }
    cout<<x<<"\n";
}