#include <bits/stdc++.h>
using namespace std;

#define fastio() ios::sync_with_stdio(false);cin.tie(0); cout.tie(0);
#define loop(i,s,n) for(int i = s;i<n;i++)
#define ll long long int
typedef vector<ll> vll;
int main()
{   
    fastio();
    int t,n;
    int temp;
    cin>>t;
    while(t--)
    {
        ll ans = 0;
        cin>>n; 
        vll d(n+1);
        loop(i,0,n)
        {
            cin>>temp;
            d[temp]++;
        }
        loop(i,1,n)ans+=d[i]*(d[i]-1)/2*d[i+1];
        loop(i,1,n+1)ans+=d[i]*(d[i]-1)*(d[i]-2)/6;
        loop(i,2,n)ans+=(d[i-1]*d[i]*d[i+1])+(d[i-1]*d[i+1]*(d[i+1]-1)/2)+(d[i-1]*d[i+1]*(d[i-1]-1)/2);
        loop(i,2,n+1)ans+=d[i]*d[i-1]*(d[i]-1)/2;
        cout<<ans<<endl;
    }

    return 0;
}