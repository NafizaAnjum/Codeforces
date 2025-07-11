#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int c=0;
    int a[]={100,20,10,5,1};

    for(int i=0; i<5; i++){
        c+=n/a[i];
        n=n%a[i];
    }
    

    cout<<c;

    return 0;
}