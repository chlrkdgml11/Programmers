nums = [3,1,2,3]

nums_set = list(set(nums))

if len(nums_set) < (len(nums) / 2):
    print(len(nums_set))

else:
    print(len(nums) // 2)

