#Runtime: 24 ms, faster than 98.35% of Python3 online submissions for String to Integer (atoi).
#Memory Usage: 14.3 MB, less than 24.28% of Python3 online submissions for String to Integer (atoi).

class Solution:
    def myAtoi(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        i = 0
        sign = 1
        result = 0
        maxint = 2**31 - 1
        minint = -2**31
        
        while i < length and s[i] == ' ': i += 1
        
        if i < length and (s[i]=='-' or s[i]=='+'):
            sign = -1 if s[i]=='-' else 1
            i += 1
        
        while i < length and s[i] >= '0' and s[i] <= '9':
            if result > maxint//10 or (result == maxint//10 and ord(s[i])-ord('0') > maxint % 10):
                return maxint if sign == 1 else minint
            result = result *10 + int(ord(s[i])-ord('0'))
            i += 1
        return result * sign
