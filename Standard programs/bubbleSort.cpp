#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    int n,temp;
    cin>>n;
    vector<int> vec;
    for(int i = 0;i<n;i++)
    {
        cin>>temp;
        vec.push_back(temp);
    }

    for(int i = 0;i<n;i++)
    {
        for(int j = i;j<n;j++)
        {
            if (vec[i]>vec[j])
            {
                temp = vec[i];
                vec[i] = vec[j];
                vec[j] = temp;
            }
        }
    }
    for(auto& it:vec)cout<<it<<" ";
    return 0;
}