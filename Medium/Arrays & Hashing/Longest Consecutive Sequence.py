from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def has(s, arr):
            start = arr[s]
            seq = set()
            for i in arr:
                if i == start:
                    seq.add(start)
                    start+=1
            return seq

        seq = set(nums)
        has_seq = {}
        if len(seq) == 0:
            print(0)
            return 0
        else:
            lists = sorted(seq)
            print(lists)
            for n in range(len(lists)):
                s = has(n, lists)
                has_seq[lists[n]] = s
            
            # print(has_seq)
            max_len = max(has_seq, key=lambda k: len(has_seq[k]))
            print(max_len)
            print(has_seq[max_len])
            print(len(has_seq[max_len]))
            return len(has_seq[max_len])