#include <bits/stdc++.h>
using namespace std;

#define fastio() ios::sync_with_stdio(false);cin.tie(0); cout.tie(0);
#define loop(i,n) for(int i = 0;i<n;i++)
#define pb push_back
typedef vector<vector<int>> vvi;
typedef vector<vector<long long>> vvll;
typedef vector<long long> vll;

int main()
{   
    fastio();
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n; 
        vll u(n),s(n);
        
        loop(i,n)
        {
            cin>>u[i];
            --u[i];
        }
        loop(i,n)cin>>s[i];
        vvi total(n);
        loop(i,n) total[u[i]].pb(s[i]);
        loop(i,n)sort(total[i].begin(),total[i].end(),greater<int>());
        vvll sums(n,vll(1,0));
        loop(i,n)for(int it:total[i])sums[i].pb(sums[i].back()+it);
        vll ans(n);
        loop(i,n)for(int j = 1;j<=int(total[i].size());++j)ans[j-1] += sums[i][total[i].size()/j*j];
        loop(i,n)cout<<ans[i]<<" ";
        cout<<endl;
    }

    return 0;
}