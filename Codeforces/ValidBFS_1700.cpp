#include<bits/stdc++.h>
#include<unordered_set>
using namespace std;

int main()
{   
    int n;
    cin>>n;
    vector<unordered_set<int>> pc(n+1);
    for(int i = 0;i<n-1;i++)
    {
        int a,b;
        cin>>a>>b;
        pc[a].insert(b);
        pc[b].insert(a);

    }
    vector<int> final;
    for(int i = 0;i<n;i++)
    {
        int temp;
        cin>>temp;
        final.push_back(temp);

    }
    unordered_set<int> visited;
    int front,back;
    front = 1;
    back = 1;
    visited.insert(1);
    if (final[0] !=1)
    {
        cout<<"No";
        return 0;
    }
    for(auto& i : final)
    {
        front = back;
        if (i!=1)
        {
            back += pc[i].size()-1;
        }
        else
        {
            back += pc[i].size();
        }
        for (int num = front;num<back;num++)
        {
            if (pc[i].find(final[num])==pc[i].end())
            {
                cout<<"No";
                return 0;
            }
        }
    }
    cout<<"Yes";
    return 0;
}