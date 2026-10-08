class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a=set(nums)
        if len(a)==len(nums):
            return False
        return True
                