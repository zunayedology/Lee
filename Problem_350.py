"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

class Solution:
    def intersect(self, nums1, nums2):
        count1 = {}
        for num in nums1:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1
        
        count2 = {}
        for num in nums2:
            if num in count2:
                count2[num] += 1
            else:
                count2[num] = 1
        
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection
