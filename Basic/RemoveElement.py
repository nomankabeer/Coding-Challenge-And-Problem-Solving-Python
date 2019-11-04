
def removeElement(nums, val):
    for key, num in enumerate(nums):
        print(num)
        # print(key)
        if(num == val):
            del nums[key]
    return nums


nums = [1,2,2,3,3,3,4,5,5,5,6,7,8,9]
print(removeElement(nums, 5))
