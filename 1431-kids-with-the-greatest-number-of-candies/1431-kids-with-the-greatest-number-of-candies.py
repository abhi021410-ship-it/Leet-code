class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        a=[]
        for i in candies:
            if i + extraCandies>=max(candies):
                a.append(True)
            else:
                a.append(False)
        return a