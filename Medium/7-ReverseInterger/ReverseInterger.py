class Solution(object):
    def reverse(self, x):
        rev = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        return rev if -2**31 <= rev <= 2**31 - 1 else 0
        