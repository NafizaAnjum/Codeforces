#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin>>s;

    for(int i=0; i<s.size(); i+=2){
        int min_i = i;
        for(int j=i+2; j<s.size(); j+=2){
            if(s[min_i]>s[j]){
                min_i=j;
            }
        }
        if(min_i!=i){
            swap(s[i],s[min_i]);
        }
    }
    cout<<s<<endl;
    return 0;

}
