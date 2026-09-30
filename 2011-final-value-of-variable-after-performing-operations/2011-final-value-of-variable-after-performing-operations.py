class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x=0
        for ch in operations :
            if ch=="--X"or ch=="X--": x-=1
            elif ch=="++X"or ch=="X++": x+=1
        return x

