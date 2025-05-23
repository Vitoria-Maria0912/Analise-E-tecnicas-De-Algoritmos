#include <iostream>

using namespace std;

int main() {

    int chaCerto, novoCha, numerosCertos = 0;
    cin>>chaCerto;

    for (int i = 0; i < 5; i++) {
        cin>> novoCha;
        if(novoCha == chaCerto){
            numerosCertos++;
        }
    }
    cout<<numerosCertos;
}