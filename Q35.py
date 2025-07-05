'''
35. Search Insert Position
Solved
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

class Solution(object):
    def searchInsert(self, nums, target):
        if (nums[0]>target):
            return 0
        elif(nums[-1]<target):
            return len(nums)
        def FindPlace(start,end):
            middle=(start+end)//2
            if (start==end):
                return start
            elif(nums[middle]==target):
                return middle
            elif (nums[middle]<target):
                return FindPlace(middle+1,end)
            elif (nums[middle]>target):
                return FindPlace(start,middle)
        return FindPlace(0,len(nums)-1)

            
