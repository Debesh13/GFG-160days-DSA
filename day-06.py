#problem-->> majority elements in the array

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        count1 = 0
        count2 = 0
        ele1 = 0
        ele2 = 0
        for i in range(n):
            if count1 == 0 and arr[i] != ele2:
                ele1 = arr[i]
                count1 = 1
            elif count2 == 0 and arr[i] != ele1:
                ele2 = arr[i]
                count2 = 1
            elif ele1 == arr[i]:
                count1 += 1
            elif ele2 == arr[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        count3 = 0
        count4 = 0
        lst = []
        for i in range(n):
            if arr[i] == ele1:
                count3 += 1
        for i in range(n):
            if arr[i] == ele2:
                count4 += 1
        if count3 > n/3:
            lst.append(ele1)
        if count4 > n/3:
            lst.append(ele2)
        return sorted(lst)    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
