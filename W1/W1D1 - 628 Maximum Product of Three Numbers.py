"""
Given an array of `nums`, find three numbers whose product is maximum and return the maximum product.

Example 1:
    Input: nums = [1,2,3]
    Output: 6

Example 2:
    Input: nums = [1,2,3,4]
    Output: 24

Example 3:
    Input: nums = [-1,-2,-3]
    Output: -6

constraints:
    3 <= nums.length <= 10^4
    -1000 <= nums[i] <= 1000
"""
import sys
def maximumProduct(nums:list[int]):
    sortedArr =sorted(nums)
    a = sortedArr[-1] * sortedArr[-2] * sortedArr[-3]
    b = sortedArr[0] * sortedArr [1] * sortedArr [-1]
    return max(a, b)

nums1 = [1,2,3]
nums2 = [1,2,3,4]
nums3 = [-1,-2,-3]
nums4 = [-100,-98,-1,2,3,4]
print(maximumProduct(nums1))
print(maximumProduct(nums2))
print(maximumProduct(nums3))
print(maximumProduct(nums4))



