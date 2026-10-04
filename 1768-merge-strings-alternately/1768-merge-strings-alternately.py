class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=0
        b=0
        c=[]
        while a<len(word1) and b<len(word2):
            c.append(word1[a])
            c.append(word2[b])
            a+=1
            b+=1
        if a<len(word1):
            c.append(word1[a:])
        
        if b<len(word2):
            c.append(word2[b:])
        
        
        return "".join(c)
