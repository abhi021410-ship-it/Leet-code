class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        a=abs(source[0]-target[0])
        b=abs(source[1]-target[1])
        if source == target:
            return 0
        elif source[0] ==target[0] or source[1]== target[1]or a==b:
            return 1
        else :
            return 2