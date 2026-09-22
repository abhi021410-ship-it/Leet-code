class Solution:
    def isPalindrome(self, s: str) -> bool:
        z=[]
        n=s.lower()
        for ch in n:
            if ch.isalpha() == True or ch.isdigit()==True:
                z.append(ch)
        #return z
        if z==z[::-1]:
            return True
        else:return False