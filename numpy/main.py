# numpy stands for numerical python, It is a python library used for:
# - fast mathematical calculations
# - working with arrays
# - Scientific computation, ML, adn Data analysis

import numpy as np
print(np.__version__)

# 1. creating arrays
# 1D Array
list1 = [1, 2, 3, 4, 5]
print(list1)

# Now, converting this list into the array
arr_list1 = np.array(list1)
print(arr_list1)
print(type(arr_list1))

# 2D Array
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
arr_list2 = np.array([list1, list2])
# print(arr_list2)

# 3D Array
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]
arr_list3 = np.array([[list1, list2, list3]])
print(arr_list3)
print(arr_list3.ndim)       # ndim --> It is used to know the dimension of the array

# 2. numpy array properties

arr1 = np.array([[1, 2, 3.4, 4, 5], [6, 7, 8, 9, 10]])
print(arr1)
print()

print("Shape: ", arr1.shape)
print("Size: ", arr1.size)
print("DType: ", arr1.dtype)
print("n_dim: ", arr1.ndim)

# 3. Array initialization methods

# zeros array:-
zero_arr = np.zeros((2, 3))
print(zero_arr)

# one array:-
one_array = np.ones((2, 3))
print(one_array)

# Full array:-
full_arr = np.full((3, 2), 7)
print(full_arr)

# Random array:-
random_array = np.random.random((2, 3))
print(f"random_array: \n {random_array}")

# sequence_array:-
sequence_array = np.arange(0, 10, 2)
print(f"sequence_array: \n {sequence_array}")


# Identity Matrix:-
identity_matrix = np.eye((3))
print(identity_matrix)

# Empty array:-
print(np.empty(2))

# Vector, Matrix and Tensor

# Vector is said to be 1D matrix
vector = np.array([1, 2, 3])
print(f"Vector: \n{vector}")

# Matrix is said to be the 2D matrix
matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"Matrix: \n{matrix}")

# Tensor is said to be the n-dimension array(Matrix)
tensor = np.array([[[1, 2], [3, 4], [5, 6]]])
print(f"Tensor: \n {tensor}")

# Array Reshaping
arr = np.arange(12)
print(f"Original array: {arr}")

reshaped = arr.reshape((4, 3))
print(f"\n Reshaped_array: {reshaped}")

# Flattened Array:-
# It is used to convert the n-Dimensional array into the one dimensional array

flattened = reshaped.flatten()
print("Flattened Array: ", flattened)

# ravel:-
# It's return the original array(view), instead of copy, where as flatten returns the copy of the array

raveled = reshaped.ravel()
print("raveled Array: ", raveled)

# Transpose matrix

transpose = reshaped.T
print("Transpose: ", transpose)

# Numpy Array operations

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic Slicing: ", arr[2:7])
# with steps
print("With steps: ", arr[2:11:2])
# negative indexing
print("Negative Indexing: ", arr[-4])

# 2D array slicing
arr_2d = np.array([[1, 2, 3, 4, 5],
                   [6, 7 , 8, 9, 10]])
print("Specific element: ", arr_2d[1, 2])
print("Entire row: ", arr_2d[1])
print("Specific Column: ", arr_2d[:,2])

# Sorting

unsroted = np.array([3, 1, 4, 2, 1, 5, 17, 3, 4, 8])
print("Sorted Array: ", np.sort(unsroted))

arr_2d_unsorted = np.array([[1,  3], [1, 2], [3, 5]])
print("Sorted 2D Array by top-to-down: ", np.sort(arr_2d_unsorted, axis=0))  # for top to bottom sorting
print("Sorted 2D Array by Column: ", np.sort(arr_2d_unsorted, axis=1))      # for column wise sorting

# Filter
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = numbers[numbers % 2 == 0]    # Numpy allows to write expressions inside the array
print("Even numers: ", even_numbers)

# Filter with Mask
# mask is an expression which evalutes

mask = numbers > 5
print("Numbers greater than by 5 :", numbers[mask])

# Fancy indexing vs np.where()

indices = [0, 2 ,4]
print(numbers[indices])

# np.where() --->    in this we give the condition and if it is true than executes
where_result = np.where(numbers > 3)
print("NP Where: ", numbers[where_result])

condition_array = np.where(numbers > 5, numbers*2, numbers)
print(condition_array)


