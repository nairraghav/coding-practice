"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters
Medium

8815

533

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        max_length = 0
        for starting_character_index in range(len(s) - 1):
            visited_characters = {s[starting_character_index]}
            length = 1
            for ending_character_index in range(starting_character_index + 1, len(s)):
                if s[ending_character_index] not in visited_characters:
                    length += 1
                    visited_characters.add(s[ending_character_index])
                else:
                    break
            max_length = max(max_length, length)

        return max_length

