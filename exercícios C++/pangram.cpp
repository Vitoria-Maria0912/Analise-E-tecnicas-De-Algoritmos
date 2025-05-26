#include <iostream>
#include <set>
using namespace std;

bool isPangram(string entrada){
    
    for (char &l : entrada) { l = tolower(l); }

    set<char> letras (entrada.begin(), entrada.end());

    return (letras.size() == 26);
}

int main(){

    int n; string entrada;

    cin>>n;

    cin>>entrada;

    if (n >= 26 && entrada.size() == n && isPangram(entrada)) { cout<<"YES\n"; }
    else { cout<<"NO\n"; }
}