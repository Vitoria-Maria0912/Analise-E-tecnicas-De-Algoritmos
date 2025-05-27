#include <iostream>
using namespace std;

int main(){
    int x, y;

    cin>>x;
    cin>>y;

    if(abs(x) > 100 || abs(x) > 100 ) {}
    else if(x == 0 || y == 0) { cout<<"eixos\n"; }
    else if(x > 0 && y > 0) { cout<<"Q1\n"; }
    else if(x < 0 && y > 0) { cout<<"Q2\n"; }
    else if(x < 0 && y < 0) { cout<<"Q3\n"; }
    else if(x > 0 && y < 0) { cout<<"Q4\n"; }
    
}