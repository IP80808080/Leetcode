class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prev = strs[0]
        for i in strs[1:]:  
            while not i.startswith(prev):
                print(prev)