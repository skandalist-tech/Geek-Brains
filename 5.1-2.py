n = 11
nums_gen = (num for num in range(1, n, 2))

print(nums_gen.__next__())
print(nums_gen.__next__())
print(nums_gen.__next__())
print(nums_gen.__next__())
print(nums_gen.__next__())
print(nums_gen.__next__())
print(next(nums_gen))