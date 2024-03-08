"""
3005. Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
"""


class Solution:
    def maxFrequencyElements(self, nums) -> int:
        freq_dic = {}
        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 1
            else:
                freq_dic[num] += 1

        max_freq = max(freq_dic.values())
        
        count = 0
        for freq in freq_dic.values():
            if freq == max_freq:
                count += freq
        
        return count
