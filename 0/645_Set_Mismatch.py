"""
Question:

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4

"""


def findErrorNums(nums):
    # duplication
    duplicate = sum(nums) - sum(set(nums))
    # correct number
    nums.sort()
    prev_num = nums[0]
    if nums[0] != 1:
        return [duplicate, 1]
    elif nums[-1] != len(nums):
        return [duplicate, len(nums)]
    else:
        for x in range(1, len(nums)):
            cur_num = nums[x]
            if cur_num - prev_num == 2:
                correct_num = prev_num + 1
                return [duplicate, correct_num]
            prev_num = cur_num



print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))