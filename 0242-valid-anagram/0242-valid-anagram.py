class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if sorted(s)==sorted(t):
            #return True
        #return False
        if len(s)!=len(t):
            return False
        sm={}
        tm={}
        for char in s:
            sm[char]=sm.get(char,0)+1
        for char in t:
            tm[char]=tm.get(char,0)+1
        for key in sm:
            if sm[key] != tm.get(key,0):
                return False
        return True
