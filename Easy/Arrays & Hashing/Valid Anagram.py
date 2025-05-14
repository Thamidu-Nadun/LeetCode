class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_has = []
        t_has = []
        for i in s:
            s_has.append(i)
        for i in t:
            t_has.append(i)
        __s = sorted(s_has)
        __t = sorted(t_has)

        print(__s)
        print(__t)
        if sorted(__s) == sorted(__t):
            return True
        else:
            return False
