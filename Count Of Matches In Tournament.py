class Solution:
    def numberOfMatches(self, n: int) -> int:
        match_count = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
                match_count += n
            else:
                n = (n-1)/2
                match_count += n
                n += 1
        return int(match_count)
