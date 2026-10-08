class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
        #if len(s)!=len(t):
            #return False
        #sm={}
        #tm={}
        #for char in s:
