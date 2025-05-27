#include <iostream>
#include <sstream>
using namespace std;

int main(){

    string entrada;
    
    getline(cin, entrada);
    
    stringstream ss(entrada);

    int P1, C1, P2, C2;
    ss >> P1 >> C1 >> P2 >> C2;

    double peso = ((P1 * C1) - (P2 * C2));

    if(peso == 0){ cout<<"0\n"; }
    else if(peso < 0){ cout<<"1\n"; }
    else { cout<<"-1\n"; }
}
