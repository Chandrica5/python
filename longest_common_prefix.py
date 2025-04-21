class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        i = 0
        while True:
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    result = ""
                    for j in range(i):
                        result += strs[0][j]
                    return result
            i += 1
