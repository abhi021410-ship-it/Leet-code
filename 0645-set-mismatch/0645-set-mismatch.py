class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        originalsum=n*(n+1)//2
        actual=sum(nums)
        uni=sum(set(nums))
        return [actual-uni,originalsum-uni]