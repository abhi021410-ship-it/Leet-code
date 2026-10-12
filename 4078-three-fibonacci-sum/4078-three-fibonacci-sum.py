class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n%2:
            return False
        n//=2
        a,b=1,2
        while a<n:
            a,b=b,a+b
        return a==n
        