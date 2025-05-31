'''
Median of Two Sorted Arrays..........................................................

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merg = sorted(nums1 + nums2)
        length = len(merg)
        if (length==0):
            return float(0)
        if (length%2==0):
            midindex1=length // 2
            midindex2=midindex1 - 1
            return (merg[midindex1] + merg[midindex2])/2.0
        else:
            midindex=length//2
            return float(merg[midindex])