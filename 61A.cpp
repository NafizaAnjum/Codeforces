#include<bits/stdc++.h>
using namespace std;

int main(){
    string a,b;
    cin>>a>>b;
    int n=a.size();

    string r = "";

    for(int i=0; i<n; i++){
        if(a[i]!=b[i]) r+='1';
        else r+='0';
    }

    cout<<r<<endl;

    return 0;
}