import numpy as np
import matplotlib.pyplot as plt
# Advance operation with Business examples

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], # Paradise Biryani
    [2, 120000, 140000, 160000, 190000], # Beijing Bites
    [3, 220000, 230000, 150000, 300000], # Pizza Hub
    [4, 180000, 440000, 260000, 290000], # Burger Point
    [5, 180000, 110000, 180000, 230000], # Chai Point
])

print("=== Zomato Sales Analysis ===")
print("\n Sales Data Shape: ", sales_data.shape)

# Now, printing the 1st 3 restaurant sales data
# print("\n Sample data for 1st 3 restaurant: ", sales_data[:3])

# Total Sales per year
print(np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0)
print(yearly_total)
# print(np.sum(yearly_total))

# Minimum sales per restaurant

min_sales = np.min(sales_data[:, 1:], axis=1)
print(min_sales)

# Maximum sales per year

max_sales_perYear = np.max(sales_data[:, 1:], axis=0)
print(max_sales_perYear)

# Average Sales per restaurant
avg_sales = np.mean(sales_data[:, 1:], axis=1)

# Cumulative sales
cumulative_sales = np.cumsum(sales_data[:, 1:], axis=1)
print(cumulative_sales)

plt.figure(figsize=(8, 6))
plt.plot(np.mean(cumulative_sales, axis=0))
plt.title("Average cumulative sales accross all restaurant ")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()