class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []
        tmp = 0
        for gains in gain:
            altitude.append(tmp)
            tmp += gains
        altitude.append(tmp)
        altitude.sort()
        return altitude[-1]
      
