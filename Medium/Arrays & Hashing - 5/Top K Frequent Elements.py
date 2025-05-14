from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        print(count)
        arr = []
        for val, count_val in count.items():
            arr.append([count_val, val])
        arr.sort()
        print(arr)
        ret = []
        while len(ret) < k:
            i = arr.pop()
            ret.append(i[1])
        return sorted(ret)
        

