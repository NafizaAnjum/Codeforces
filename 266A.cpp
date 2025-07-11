#include<bits/stdc++.h>
using namespace std;

int main()
{
   int n;
   string s;
   cin>>n>>s;

   int c=0;
   for(int i=0; i<s.size(); i++){
    if(s[i]==s[i+1])
    c++;
   } 
   cout<<c<<endl;
   return 0;
}