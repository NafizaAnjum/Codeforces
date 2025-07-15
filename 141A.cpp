#include<bits/stdc++.h>
using namespace std;

int main(){
     string str,str1,str2;
     cin>>str1>>str2>>str;

     str1+=str2;

     sort(str1.begin(),str1.end());
     sort(str.begin(),str.end());

     if(str1==str)
        cout<<"YES"<<endl;
    else 
        cout<<"NO"<<endl;

    return 0;
}