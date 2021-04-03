#The time complexity is O(n) and space complexity is also less than others.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = 0
        while i<len(A):
            if A[i]%2 == 0:
                A[j], A[i] = A[i], A[j]
                j += 1
            i += 1
        return A
        
