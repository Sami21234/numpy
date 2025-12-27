import numpy as np
import matplotlib.pyplot as plt

try:
    logo = np.load('numpy-logo.npy')
    print(logo.shape)
    print(logo.dtype)
    # Display
    plt.figure(figsize=(8, 6))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy logo")
    plt.grid(False)
    plt.show()

    dark_logo = 1 - logo
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy Dark logo")
    plt.grid(False)
    plt.show()

except FileNotFoundError:
    print("numpy logo file not found")

