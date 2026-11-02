class Solution:
    def minMoves2(self, arr: list[int]) -> int:
        arr.sort()
        mid=arr[len(arr)//2]
        moves=0
        for num in arr:
            moves+=abs(num-mid)
        return moves