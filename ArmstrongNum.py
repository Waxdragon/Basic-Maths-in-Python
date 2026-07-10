class Solution:
    def isArmstrong(self, n):
        original = n
        count = 0
        temp = n
        while temp > 0:
            count += 1
            temp //= 10
        temp = n
        num = 0
        while temp > 0:
            digit = temp % 10
            num += digit ** count
            temp //= 10
        return num == original