class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxi=0
        cnt=0
        for i in nums:
            if i ==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi