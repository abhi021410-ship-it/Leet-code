class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        k=n//2
        ts=sum(nums)
        halfs=sum(nums[:k])
        cnt=0
        for i in range(n):
            if 2*halfs>ts:
                cnt+=1
            halfs+=nums[(i+k)%n]-nums[i]
        return cnt