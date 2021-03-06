#include <bits/stdc++.h>

using namespace std;

int store[1001][1001];

int dp(int r1, int r2, int n, int ma[], int mb[]) 
{
    if (r1 == n-1 or r2 == n-1)
        return 0;
    if (r1 == -1 and r2 == -1)
        return min(abs(ma[0]-mb[0])+dp(r1,0,n,ma,mb),abs(ma[0]-mb[0])+dp(0,r2,n,ma,mb));
    if (r1 == -1 and r2 >= 0)
        return min(abs(ma[r2+1]-mb[r2+1])+dp(r2+1,r2,n,ma,mb),abs(ma[r2+1]-mb[r2])+abs(ma[r2+1]-mb[r2+1])+dp(r1,r2+1,n,ma,mb));
    if (r1 >= 0 and r2 == -1)
        return min(abs(ma[r1+1]-mb[r1+1])+dp(r1,r1+1,n,ma,mb),abs(ma[r1+1]-mb[r1])+abs(ma[r1+1]-mb[r1+1])+dp(r1+1,r2,n,ma,mb));
    if (store[r1][r2] != -1){
        return store[r1][r2];}
    store[r1][r2] = min(abs(ma[max(r1,r2)+1]-mb[r1])+abs(ma[max(r1,r2)+1]-mb[max(r1,r2)+1])+dp(max(r1,r2)+1,r2,n,ma,mb),abs(ma[max(r1,r2)+1]-mb[r2])+abs(ma[max(r1,r2)+1]-mb[max(r1,r2)+1])+dp(r1,max(r1,r2)+1,n,ma,mb));
    return store[r1][r2];
}

int main()
{
    int t, m, n;
    cin >> t;
    while (t--) 
    {
        cin >> m >> n;
        int ma[n], mb[n];
        for (int i = 0; i < n; i++) 
	{
            cin >> ma[i] >> mb[i];
        }
        memset(store, -1, sizeof(store));
        cout << dp(-1, -1, n, ma, mb) << endl;
    }
}
