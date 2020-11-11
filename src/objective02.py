"""
Describe the difference between in-place and out-of-place algorithms
"""




"""
Given a list of nums

Triple them
"""


"""INPLACE"""
# iterate over nums
# pulling index
# set nums at index to
# nums at index X 3
n = [1,2,3]

def tripple_in_place(nums):
    for index in range(len(nums)):
        nums[index] = nums[index] * 3
    # no need to return do to in-place

print(n)
x = tripple_in_place(n)
print(n)
print(x)




"""OUT-PLACE"""
# Create new array
# iterate over nums
# pulling index
# set num_array at index to
# nums at index X 3
x = []
n = [1,2,3]

def tripple_out_place(nums):
    new_nums = [None] * len(nums)
    for index in range(len(nums)):
        new_nums[index] = nums[index] * 3
    # need to return do to out-place
    return new_nums

print(n)
x = tripple_out_place(n)
print(n)
print(x)