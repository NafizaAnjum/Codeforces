#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    int a,b;

    while(t--){
        cin>>a>>b;

        if(a%b==0) cout<<"0"<<endl;
        else{
            long long r= a%b;
            cout<<b-r<<endl;
        }
    }
    return 0;
}