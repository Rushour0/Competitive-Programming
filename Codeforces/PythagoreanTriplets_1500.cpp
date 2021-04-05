#include <bits/stdc++.h> 
using namespace std; 
 
int main() 
{ 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
 
    while(t--)
    {
        int n,v = 4;
        int c = 0;
        cin>>n;
        while(n>v)
        {
            c+=1;
            v = 2*(c+1)*(c+2);
        }
        cout<<c<<endl;
    }
    return 0;
}