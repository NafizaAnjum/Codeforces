#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin>>n;
    long long a=0;
    
    if(n%2==0)
        a=n/2;
    else a=-(n+1)/2;
    
    cout<<a<<endl;
    return 0;
    
    }