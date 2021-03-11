class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        usum = 0
        tmp = []
        cnum = nums.copy()
        for num in cnum:
            if num in tmp:
                continue
            if num in nums:
                tmp.append(num)
                nums.remove(num)
            if num in nums:
                while num in nums:
                    nums.remove(num)
            else:
                usum += num
        return usum
