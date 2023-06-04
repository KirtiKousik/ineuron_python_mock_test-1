def moveZeroes(nums):
    nonZeroPos = 0
  
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZeroPos] = nums[i]
            nonZeroPos += 1

    while nonZeroPos < len(nums):
        nums[nonZeroPos] = 0
        nonZeroPos += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums = [0]
moveZeroes(nums)
print(nums)
