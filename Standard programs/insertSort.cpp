#include <bits/stdc++.h>
#define ll long long int
#define getarr(arr) for(auto &i:arr)cin>>i;
#define putarr(arr) for(auto &i:arr)cout<<i<<" ";
using namespace std;

int main()
{
  ll n,counter,temp;
  cin>>n;
  int toBeSorted[n];  
  getarr(toBeSorted);
  for(int i = 1; i<n;i++)
  {
    counter = i;
    for(int j = i-1;j>=0;j--)
    {
      
      if (toBeSorted[j]>toBeSorted[counter])
      {
        temp = toBeSorted[j];
        toBeSorted[j] = toBeSorted[counter];
        toBeSorted[counter] = temp;
      }
      else break;
      counter-=1; 
      //else break;
    }
  }
  putarr(toBeSorted);
  cout<<endl;
  
  return 0;
}