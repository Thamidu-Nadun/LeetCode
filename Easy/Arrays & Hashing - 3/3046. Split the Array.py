class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ht = {}

        for i in nums:
            if i in ht:
                ht[i]+=1
                if ht[i] >2: return False
            else:
                ht[i] = 1
        return True
