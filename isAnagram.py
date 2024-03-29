class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = dict()
        d2 = dict()
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for j in t:
            if j in d2:
                d2[j] +=1
            else:
                d2[j] = 1
        return d1 == d2


                