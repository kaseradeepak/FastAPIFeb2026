import time
import numpy as np

# 1M -> 10^6
# 100M -> 100 * 10^6
# start_time = time.time()
# arr1 = [i for i in range(100000000)] # 100 million elements in arr1 
# arr2 = [i for i in range(100000000, 200000000)] # 100 million elements in arr2 

# arr3 = []
# for i in range(100000000):
#     arr3.append(arr1[i] + arr2[i]) # # 100 million elements in arr3

# end_time = time.time()

# print(end_time - start_time)

# start_time = time.time()

# arr1 = np.arange(100000000)
# arr2 = np.arange(100000000, 200000000)

# arr3 = arr1 + arr2

# end_time = time.time()

# print(end_time - start_time)

# arr = [1, 2, 3]
# print(type(arr))

# arr1 = np.array([1, 2, 3]) => arr[1:]
# arr2 = np.array([8, 4, 1])

# result = arr1 + arr2

# print(result) # array => [9, 6, 4]
# print(type(result))

# arr = np.array([[1,2], [3,4], [5,6]]) # 2D array

# print(arr)

# 3d array
# arr = np.array([
#     [[1,2], [3,4]],
#     [[5,6], [7,8]]
# ])

# print(arr)

# arr = np.array([[1,2], [3,4], [5,6]])

# arr = np.array([
#     [[1,2, 4], [3,4, 1]],
#     [[5,6, 8], [7,8, 9]]
# ])

# print(arr.shape) # 2 * 2 * 3

# print(arr.ndim)

# Data Type
# arr = np.array([1, 2, 3, 'masai', 61.0])
# print(arr.dtype)

# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([8, 4, 1])

# arr3 = arr1 + arr2 

# print(arr3)

# arr1 = np.array([[1,2], [3,4], [5,6]])
# arr2 = np.array([[4,1], [2,7], [6,2], [7,1]])

# print(arr1)
# print(arr2)

# arr3 = arr1 + arr2 

# print(arr3)

# arr1 = np.array([[1,2], [3,4], [5,6]]) # 3 * 2
# arr2 = np.array([[3], [5], [1], [2]]) # 3 * 1

# arr3 = arr1 + arr2

# print(arr3)

# Create a N dimensional array with all the zeroes 

# arr1 = np.array([[0,0], [0,0], [0,0]])

# print(arr1)

# arr = np.zeros((10, 4))
# print(arr)
# print(arr.dtype)

# arr = np.ones((3, 2), dtype=int)
# print(arr)
# print(arr.dtype)

# Array Indexing and Slicing
# arr[x:y] => all the elements from index x to y-1
# arr[-1] 

# arr = np.array(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [2, 4, 5]
#     ]
# )

# print(arr[1][2])
# print(arr[1, 2])

# print(arr[1][:2])

# arr = np.array([4, 5, 6, 8])

# print(arr + 10)
# print(arr ** 2)

# Mean, median, mode

# print(np.mean(arr))
# print(np.median(arr))
# print(np.sum(arr))
# print(np.average(arr))

arr = np.array([[1,2], [3,4], [5,6]])
# print(arr)

# Flatten
flat1 = arr.flatten()
# Flatten -> doesn't change the original array, rather it creates a copy array and then it flattens the copy array.

# ravel
flat2 = arr.ravel()

# print(flat1)
# print(flat2)

# flat1[0] = 100
# flat2[0] = 200

# print(flat1)
# print(flat2)
# print(arr)

# Flatten -> Creates a copy
# Ravel -> No copy => More efficient than flatten
# np.random.rand() -> returns a random number between 0 & 1
# print(np.random.rand(5, 2, 3))