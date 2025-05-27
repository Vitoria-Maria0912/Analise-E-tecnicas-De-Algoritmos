#include <iostream>
using namespace std;

int main(){

    double A, B;
    cin>>A;
    cin>>B;
    
    double media = (A + B)/2;

    if(media >= 7){ cout<< "Aprovado\n"; }
    else if(media >= 4){ cout<< "Recuperacao\n"; }
    else { cout<<"Reprovado\n"; }
}