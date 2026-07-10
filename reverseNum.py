class Solution:
    def reverseNumber(self, n):
        original = str(n)
        revnum = 0
        while(n>0):
            lastdig = n%10
            revnum = (revnum*10)+lastdig
            n = n//10
        return revnum
