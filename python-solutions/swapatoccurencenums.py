def swapatoccurence(nums: list, val: int):
    # iterate the list and count all occurent of val
    # move occurence of val to the end of list
    count = 0
    for i, element in enumerate(nums):
        if element == val:
            if i != len(nums) - 1 and nums[i + 1] != val:
                temp = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = temp
                count += 1
    
    return nums
