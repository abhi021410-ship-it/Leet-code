class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        '''dp= [[None for i in range(len(piles))]for i in range(len(piles))]
        def solve(st, en):
            if st>en:
                return 0
            if dp[st][en] is not None:
                return dp[st][en]
            #choose start and then bob chooses start
            c11= solve(st+2, en)+ piles[st]
            #choose start and then bob chooses end
            c12= solve(st+1, en-1)+ piles[st]
            #choose end and bob chooses start
            c21= solve(st+1, en-1)+ piles[en]
            #both choose end
            c22= solve(st, en- 2)+ piles[en]
            dp[st][en]= max(c11, c12, c21, c22)
            return max(c11, c12, c21, c22)
        ans= solve(0, len(piles)-1)
        return True if ans> sum(piles)/2 else False'''
        return True