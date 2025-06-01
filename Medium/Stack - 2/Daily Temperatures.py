class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        class Stack:
            def __init__(self):
                self.stack = []
            def insert(self, n):
                self.stack.append(n)
                return n
            def pop(self):
                self.stack.pop(len(self.stack)-1)
            def peek(self):
                return self.stack[len(self.stack)-1]
    
        def getMax(nums):
            max_n = nums[0]
            for i in range(1, len(nums)):
                if max_n < nums[i]:
                    max_n = nums[i]
                    return max_n, i
                
            return max_n, 0
            
        # [1,4,1,2,1,0,0]
        nums = temperatures
        res = []
        stack = Stack()
        max_n, idx = stack.insert(getMax(nums))
        diif = 0
        # print(max_n, idx)
        for i in range(len(nums)):
            # print(nums[i], end=" ")
            
            maxJ, jidx = getMax(nums[i::])
            # print(maxJ, jidx)
            res.append(jidx)
                
        # print(res)
        return res