class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        add = {}

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1, j+1] # Human Index
        return []
