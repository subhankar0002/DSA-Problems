'''
Reverse Integer.........................................

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 

'''

class Solution(object):
    def reverse(self, x):
        num=abs(x)
        rev=0
        while num>0:
            a=num%10
            num=num/10
            rev=rev*10+a
        if (x<0):
            rev=-rev
        if (rev >=-2**31 and rev<=2**31-1 ):
            return rev
        else :
            return 0


