from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has = dict()
        has_list = []
        for i in strs:
            text = ''.join(sorted(i))
            if text in has:
                has[text].append(i)
            else:
                has[text] = []
                has[text].append(i)
        
        for i in has:
            has_list.append(has[i])
        return has_list