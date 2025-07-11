#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    int sum=0;
    double avg=0;
    
    
    for(int i=0; i<n; i++){
        cin>>a[i];

        sum+=a[i];
        }

    avg=(double)sum/n;
    
    cout<<fixed << setprecision(12)<<avg<<endl;

    return 0;
    
}