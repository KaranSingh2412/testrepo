#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(2*n);
        vector<int> freq(2*n+1);
        for(int i=0;i<2*n;i++){
            cin>>a[i];
            freq[a[i]]++;
        }
        int sum = 0;
        int ans = 0;
        int k1 = 0;
        for(int i = 0;i<freq.size();i++){
            if(freq[i]!=0){
                if(freq[i]%2 == 0){
                    k1++;
                }
                else{
                    sum += a[i];
                    ans++;
                }
            }
        }
        if((2*n-sum)%2==0){
            if(k1%2==0){
                ans += (k1/2)*4;
            }
            else{
                ans += ((k1-1)/2)*4;
            }
        }
        else{
            if(k1%2!=0){
                ans += (k1/2)*4;
            }
            else{
                ans += ((k1-1)/2)*4;
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}