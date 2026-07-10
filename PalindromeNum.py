class Solution:
    def isPalindrome(self, n):
        copy = n
        revnum =0
        while n>0:
            lastdigit = n%10
            revnum = (revnum*10)+lastdigit
            n = n//10
        return revnum == copy