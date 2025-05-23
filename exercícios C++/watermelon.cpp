#include <iostream>
using namespace std;

bool isPair(int num){
    bool asw = false;
    if((num % 2) == 0){ asw = true; }
    return asw;
}

bool isDividedByTwo(int num){
    bool asw = false;
    for(int i=2; i<=num; i++){
        if(isPair(num / i) ){
            asw = true;
        }
    }
    return asw;
}

int main(){

    int w;
    cin>>w;

    if(isPair(w) && isDividedByTwo(w)){ cout<<"YES"; }

    else { cout<<"NO"; }
}