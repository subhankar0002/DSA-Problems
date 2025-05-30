'''
Longest Substring Without Repeating Charecter............................................

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3

Example 4:
Input: s = " "
Output: 1

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen=0
        NewWord=""
        for i in s:
            if(i not in NewWord):
                NewWord += i
            else:
                maxlen=max(maxlen,len(NewWord))
                dup_index = NewWord.index(i)
                NewWord = NewWord[dup_index + 1:] + i
        maxlen = max(maxlen, len(NewWord))
        return maxlen
