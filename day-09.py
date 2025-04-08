#problem--->Minimize The Height 
#Time Com--:O(n logn)
#Space Com--:O(1)
class Solution:
    def getMinDiff(self, arr,k):
        # code here
      n=len(arr)
      if n==1:
          return 0
      arr.sort()
      ans=arr[-1]-arr[0]
      for i in range (n-1):
          if arr[i+1] < k:
              continue
          max_height=max(arr[i]+k,arr[-1]-k)
          min_height=min(arr[0]+k,arr[i+1]-k)
          ans=min(ans,max_height-min_height)
      return ans
