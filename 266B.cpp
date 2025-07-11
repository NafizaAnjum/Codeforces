#include<bits/stdc++.h>
using namespace std;

int main(){
    int n=0,t;
    string S;
    cin>>n>>t;
    cin>>S;
    
    while(t--){
        for(int i=0; i<n-1;i++){
             if(S[i]=='B' && S[i+1]=='G') {
         swap(S[i],S[i+1]);
         
         i++;
          }
       }
        }
        cout<<S<<endl;
        return 0;
    
}