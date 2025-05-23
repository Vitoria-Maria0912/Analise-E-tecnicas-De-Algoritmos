#include <iostream>
using namespace std;

int minSteps(int num){
    int asw = 0;
    if(num <= 5) { asw = 1; }
    else{
        for(int i = 5; i >= 1; i--){
            if(i == 0) { i = 5; }
            int div = (num / i); 
            asw += div; num -= (div * i);
        }
    }
    return asw;
}

int main(){

    ios_base::sync_with_stdio(0); cin.tie(0);
    
    int x;
    cin>>x;

    cout<<minSteps(x)<<"\n";
}