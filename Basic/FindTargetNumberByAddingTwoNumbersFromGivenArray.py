'''
 * User: Noman Kabeer
 * Date: 1-nov-2019
 * Time: 1:12 AM
 * Problem:
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 * Because nums[0] + nums[1] = 2 + 7 = 9
 * return [0, 1].
'''


def twoSum(nums, target):
    for i_index, i in enumerate(nums):
        for j_index, j in enumerate(nums):
            if (i + j == target and j_index != i_index):
                return [i_index, j_index]


nums = [1, 2, 3, 4, 5, 6, 7]
print(twoSum(nums, 3))
