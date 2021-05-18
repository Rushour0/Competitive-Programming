#include <bits/stdc++.h>
using namespace std;
#define fastio() ios::sync_with_stdio(false);cin.tie(0); cout.tie(0)


int query(int e)
{
    int sum;
    cout<<"? 1 "<<e<<endl;
    cin>>sum;
    return e-sum;   
}
void solve()
{
    int num,t,k;
    scanf("%d%d%d",&num,&t,&k);
    int s = 1,e = num;
    int mid;
    while (true)
    {
        mid = (s+e)/2;
        t = query(mid);
        if (s == e and t == k)
        {
            cout<<"! "<<s<<endl;
            return;
        }
        if (t>= k)e = mid;
        else s = mid+1;  
    }
}
int main()
{
    fastio();
    solve();
    return 0;
}

/*
1 0 1 0 1 1
*/  