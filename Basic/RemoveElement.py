'''
 * User: Noman Kabeer
 * Date: 04-nov-2019
 * Time: 1:12 AM
 * Problem:
 * Given an array nums and a value val, remove all instances of that value in-place and return the new length.
 * Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
 *
'''
def removeElement(nums, val):
    for key, num in enumerate(nums):
        print(num)
        # print(key)
        if(num == val):
            del nums[key]
    return nums


nums = [1,2,2,3,3,3,4,5,5,5,6,7,8,9]
print(removeElement(nums, 5))
