class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for s in sentences:
            wordcnt=1
            for ch in s:
                if ch==" ":
                    wordcnt+=1
            maxi=max(wordcnt,maxi)    
        return maxi
