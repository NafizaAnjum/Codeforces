#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    string x;
    cin >>x;
    set<char> s;

    for(int i=0; i<n;i++){

        s.insert(tolower(x[i]));
    }
    if(s.size()==26) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    return 0;
}