'''
Longest Palindromic Substring..................................................

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

'''My Code:
   Time :O(n^3)
   space:O(n^2)
'''
class Solution(object):
    def longestPalindrome(self, s):
        LPS=""
        max=0
        substringList=[]
        def checkPalindrom(data):
            data=data.lower()
            return data==data[::-1]
        if (checkPalindrom(s)):
            return s
        else: 
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    substringList.append(s[i:j])
            for i in substringList:
                boolean=checkPalindrom(i)
                if (boolean and max<len(i) ):
                    max=len(i)
                    LPS=i
            return LPS
        
'''
ChatGpt code:
 Manacher’s Algorithm..........
 Time: O(n)
 Space: O(n)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform string: add sentinels to handle even-length palindromes
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n  # Array to store the radius of palindromes
        center = right = 0
        max_len = 0
        center_index = 0

        for i in range(n):
            mirror = 2 * center - i  # Mirror of i around center

            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around center i
            a = i + p[i] + 1
            b = i - p[i] - 1
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary if we expanded past right
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Track the longest palindrome
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        # Extract the original substring from the transformed string
        start = (center_index - max_len) // 2
        return s[start:start + max_len]
