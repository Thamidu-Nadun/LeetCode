from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            p_arr = []
            for j in range(len(nums)):
                if i==j:
                    continue
                p_arr.append(nums[j])
            val = 1
            for n in p_arr:
                val*=n
            arr.append(val)
        return arr