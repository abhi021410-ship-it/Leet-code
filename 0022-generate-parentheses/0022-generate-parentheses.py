class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        def sol(ob,cb,arr):
            if len(arr)==2*n:
                result.append(arr)
                return
            if ob<n:
                sol(ob+1,cb,arr+"(")
            if cb<ob:
                sol(ob,cb+1,arr+")")
        sol(0,0,"")
        return result