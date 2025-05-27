#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main(){

    string entry, elements_a, elements_b, asw="";
    getline(cin, entry);

    stringstream ss(entry);

    int n, m;
    ss >> n >> m;

    vector<int> vector_a(n), vector_b(m);

    for(int i = 0; i < n; i++){ cin >> vector_a[i]; }
    for(int j = 0; j < m; j++){ cin >> vector_b[j]; }

    sort(vector_a.begin(), vector_a.end());

    for(int num_b : vector_b){
        int count = upper_bound(vector_a.begin(), vector_a.end(), num_b) - vector_a.begin();
        cout<<count<<" ";
    }
}