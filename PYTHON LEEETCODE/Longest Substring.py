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
        map ={} # created an empty dict
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in map and start >= map[s[i]]:
                start= map[s[i]] + 1
            else:
                max_length = max(max_length, i- start + 1)
                map[s[i]] = i
        return max_length        
        
