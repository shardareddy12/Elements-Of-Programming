'''


'''

nums = [3,3,1,0,2,0,1]

def canJump(nums):
    goal = len(nums) - 1
    # nums1 = nums[::-1]
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

print(canJump(nums))