class Solution(object):
    def lengthOfLongestSubstring(s):
        sub = []
        max_len = 0
        for c in s:
            sub = sub[sub.index(c)+1:] + [c] if c in sub else sub + [c]
            max_len = max(max_len, len(sub))
        return max_len, sub                  
        
solution = Solution()
s = input("Enter String: ")
print(solution.lengthOfLongestSubstring(s))