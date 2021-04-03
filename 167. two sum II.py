class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if numbers[i]==0:
                if numbers[i]+numbers[i+1]==target:
                    return [i+1,i+2]
                continue
            for j in range(i+1,len(numbers)):
                if target == numbers[i]+numbers[j]:
                    return [i+1,j+1]
