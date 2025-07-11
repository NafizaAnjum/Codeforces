#include<bits/stdc++.h>
using namespace std;
int main(){
    int n=0;
    int c=0;
    int a[100];
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int i=0; i<n; i++){
        if(a[i]==1)
        c++;
    }
    if(c==0) cout<<"EASY";
    else cout<<"HARD";
    return 0;
     
}