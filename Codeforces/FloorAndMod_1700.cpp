#include<bits/stdc++.h>
using namespace std;
int main()
{   ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while (t--)
    {   
        long long int a,b,zero = 0;
        cin>>a>>b;
        long long int c = 0;
        for (long long int i = 1;i*i<a;i++)
        { 
          c+=max(zero,min(b,a/i-1)-i);
        }
        cout<<c<<endl;
    }
    return 0;
}