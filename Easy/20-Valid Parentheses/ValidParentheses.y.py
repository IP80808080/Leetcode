class Solution(object):
    def isValid(self, s):
        ls = []
        c = {
        "(": ")",
        "[": "]",
        "{": "}"
        }
        for i in s:
            if i in c:
                ls.append(i)
            elif i in c.values():
                if ls and c.get(ls[-1]) == i:
                    ls.pop()
                else:
                    return False
        return len(ls) == 0

#or 

#class Solution(object):
#    def isValid(self, s):

#        stack = []
#        hash_map = {"}":"{", ")":"(", "]":"["}

#        for parenthesis in s:
#            if parenthesis in hash_map:
#                if stack and stack[-1] == hash_map[parenthesis]:
#                    stack.pop()
#                else:
#                    return False 
#            else:
#                stack.append(parenthesis)
#        if not stack:
#            return True
#        else:
#            return False