# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# use zip 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            letters = ''

            for i in zip(*strs):
                if len(set(i)) == 1:
                    letters +=i[0]
                else:
                    break
            return letters
        