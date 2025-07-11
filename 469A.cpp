#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,p, q;
    cin>>n;
    set<int> s;

    cin>>p;
    for(int i=0; i<p; i++){
        int x;
        cin>>x;
        s.insert(x);
    }

    cin>>q;
    for(int i=p; i<p+q; i++){
        int y;
        cin>>y;
        s.insert(y);
    }
 
    
    if(n==s.size()){
        cout<<"I become the guy."<<endl;
    }
    else cout<< "Oh, my keyboard!"<<endl;

    return 0;
}