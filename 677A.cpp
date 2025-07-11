#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,h;
    int c=0;
    cin>>n>>h;
    int a[100];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int i=0; i<n; i++){
        if(a[i]>h)
        c+=2;
        else c++;
    }
    cout <<c<<endl;
    return 0;
    
}