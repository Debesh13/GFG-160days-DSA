class Solution {
    public:
      int maximumProfit(vector<int> &prices) {
          // code here
          int maxele = 0, maxprofit = 0;
          for(int i = prices.size() - 1; i >= 0; i--){
              //update maximum element
              maxele = max(maxele, prices[i]);
              //update maximum profit
              maxprofit = max(maxprofit, maxele - prices[i]);
          }
          return maxprofit;
          
      }
  };