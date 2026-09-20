class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap={}
        for i in range(len(nums)):
            current=nums[i]
            need=target-current
            if need in prevMap:
                return [prevMap[need],i]
            prevMap[current]=i