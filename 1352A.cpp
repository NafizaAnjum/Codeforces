#include<bits/stdc++.h>
using namespace std;

int main(){
    int t=0;
    cin>>t;
    while(t--){
    int n;
    cin>>n;
    vector<int> v;

    int j=0;
    while(n>0){
        if(n%10){
        int r=pow(10,j);
        r=r*(n%10);
        v.push_back(r);
        } 

    n/=10;
    ++j;
    }
    
    int len=v.size();
    cout<<len<<endl;

    for(int i=len-1; i>=0; i--){
        cout<<v[i]<<" ";
    }
    cout<<endl;
    }
    return 0;
}