class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        
        res = arr[0]
        maxending = arr[0]
        for i in range(1, len(arr)):
            maxending = max(maxending + arr[i] , arr[i])
            
            res = max(res, maxending)
        return res