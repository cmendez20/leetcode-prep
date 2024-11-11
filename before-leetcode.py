### ARRAY INDEXING

# Iterate Over an Array
# Write a function that prints each element in an array in order from the first to the last.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = [4, 8, 6, 7, 9, 15]


def iterateOverArray():
    for x in nums:
        print(x)


# iterateOverArray()


# Iterate Over an Array in Reverse
def iterateOverArrayReverse():
    for x in reversed(nums):
        print(x)
    # for i in range(len(nums) - 1, -1, -1):
    #     print(nums[i])


# iterateOverArrayReverse()


# Fetch Every Second Element
def fetchSecondElement():
    for i in range(0, len(nums) - 1, 2):
        print(nums[i])


# fetchSecondElement()

# Find the Index of a Target Element
# Iterate over an array and find the first prime number. Stop the iteration once you find it.
# def findTarget():
#     for x in primes:
#         if x > 1 and x :

# traverse a Two-Dimensional Array
# write a function to print all elements of a 2D array (matrix), row by row.
