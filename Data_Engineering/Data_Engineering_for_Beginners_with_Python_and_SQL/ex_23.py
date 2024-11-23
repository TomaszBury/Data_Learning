def find_closest(nums, target):
    if len(nums) == 0:
        return None
    # Initialize the closest number with the first element in the list
    closest_num = nums[0]
    # Initialize the minimum difference with the difference of the first element and the target
    min_diff = abs(abs(nums[0]) - abs(target))

    # Iterate through the list to find the closest number
    for num in nums:
        current_diff = abs(abs(num) - abs(target))
        if current_diff < min_diff:
            min_diff = current_diff
            closest_num = num

    return closest_num

assert find_closest([2, 4, 8, 10], 6) == 4
assert find_closest([], 0) == None