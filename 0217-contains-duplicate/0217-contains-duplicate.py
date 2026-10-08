class Solution:
    #def containsDuplicate(self, nums: list[int]) -> bool:
        #a=set()
        #for i in nums:
            #if i in a:
                #return True
            #a.add(i)
        #return False
    def containsDuplicate(self, nums: list[int]) -> bool:
        a=set(nums)
        if len(a)==len(nums):
            return False
        return True