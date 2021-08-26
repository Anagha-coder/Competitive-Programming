# leetcode python
#Longest Substring Without Repeating Characters

# visit    https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        map = {}
        start = max_length = 0
        for i,c in enumerate(s):
            if c in map and start <= map[c]:
                start = map[c]+1
            else:
                max_length = max(max_length,i-start+1)
            map[c] = i
        return max_length
