class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        t=0
        for i in hours:
            if i>=target:
                t+=1
        return t
            
