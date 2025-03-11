#include<bits/stdc++.h>
using namespace std;

void sortColors(vector<int>&arr){
    int countZero = 0;
    int countOne = 0;
    int countTwo = 0;

    for(int i=0;i<arr.size();i++){
        if(arr[i]==0)countZero++;
        else if (arr[i]==1)countOne++;
        else countTwo++;
    }

    for(int i=0;i<countZero;i++){
        arr[i] = 0;
    }

    for(int i=countZero;i<countZero+countOne;i++){
        arr[i] = 1;
    }

    for(int i=countZero+countOne;i<arr.size();i++){
        arr[i] = 2;
    }
}


int main(){

    vector<int>arr = {0,1,2,0,1,2,1,2,0,0,0,1};
   sortColors(arr);

   for(int i=0;i<arr.size();i++){
    cout<<arr[i];
   }
}