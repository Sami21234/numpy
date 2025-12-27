import numpy as np

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], # Paradise Biryani
    [2, 120000, 140000, 160000, 190000], # Beijing Bites
    [3, 220000, 230000, 150000, 300000], # Pizza Hub
    [4, 180000, 440000, 260000, 290000], # Burger Point
    [5, 180000, 110000, 180000, 230000], # Chai Point
])

# Adding and Removing Data

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
combined = np.concatenate((arr1, arr2))
print(combined)

# Array compatibility

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([7, 8, 9])

print("Compatibility Shapes: ", a.shape == b.shape)

# Adding rows in the original Array
original = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
new_row = np.array([[5, 6, 7, 8, 9]])
with_new_row = np.vstack((original, new_row))      # vstack--> Stack arrays in sequence vertically (row wise).
print(original)
print()
print(with_new_row)

# Adding colmuns in the original array
new_col = np.array([[9], [9]])
with_new_col = np.hstack((original, new_col))    # hstack--> Stack arrays in sequence horizontally (column wise).
print(original)
print()
print(with_new_col)

# Now, Deleting the item

arr = np.array([11, 2, 4, 6, 6, 78])
deleted = np.delete(arr, 2)  # removes the element at the specific  index(start, stop, step)
print("Array after deletion: ",deleted)

# Vector

vector1 = np.array([1, 2, 3, 4, 5, 7])
vector2 = np.array([7, 8, 9, 10, 11, 13])
print()
print("Vector Addition: ", vector1 + vector2)
print("\nVector Multiplication: ", vector1 * vector2)
print("\nDot Product: ", np.dot(vector1, vector2))

vector_angle = np.arccos(np.dot(vector1, vector2)/( np.linalg.norm(vector1)* np.linalg.norm(vector2)))
print(vector_angle)

# Vectorized Operations(means the operation performed on each items in the matrix)
restaurant_types = np.array(["biryani", "chinense", "pizza", "burger", "cafe"])
vector_upper = np.vectorize(str.capitalize)
print("Vectorized Upper: ", vector_upper(restaurant_types))

monthly_avg = sales_data[:, 1:] / 12
trunc = np.round(monthly_avg)
print(trunc)
