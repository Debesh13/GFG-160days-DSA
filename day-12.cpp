class Solution {
    public:
      // arr: input array
      // Function to find maximum circular subarray sum.
      int circularSubarraySum(vector<int> &arr) {
  
          // your code here
          
          int totalsum = 0;
          int currMaxSum = 0, currMinSum = 0;
          int maxSum = arr[0], minSum = arr[0];
          
          for(int i =0; i < arr.size(); i++){
              currMaxSum = max(currMaxSum + arr[i], arr[i]);
              maxSum = max(maxSum, currMaxSum);
              
              currMinSum = min(currMinSum + arr[i], arr[i]);
              minSum = min(minSum, currMinSum);
              
              totalsum = totalsum + arr[i];
          }
          
          int normalSum = maxSum;
          int circularSum = totalsum - minSum;
          
          if(minSum == totalsum)
              return normalSum;
              return max(normalSum, circularSum);
          
          
          
      }
  };