#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    string s;

    for(int i=0;i<n;i++){
        if(i%2==0) s+="I hate ";
        else s+="I love ";

        if(i!=n-1) s+="that ";
        else s+="it";
    }
    cout<<s<<endl;
    return 0;
}