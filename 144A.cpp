#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[100];
    int mini=0;
    int maxi=0;

    for(int i=0; i<n; i++){
        cin>>a[i];
        if(a[i]>a[maxi]) {
            maxi=i;
        }
        if(a[i]<=a[mini]){
            mini=i; 
        }
    }

    int c=n-1-mini+maxi;
     if(maxi>mini) c--;

     cout<<c<<endl;

     return 0;
}