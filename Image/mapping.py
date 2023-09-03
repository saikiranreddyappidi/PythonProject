import numpy as np
import matplotlib.pyplot as plt

# Define the data
arr = [[187, 188, 189, 191, 191, 191, 192, 191, 190, 188],
       [190, 192, 193, 194, 195, 195, 196, 194, 193, 192],
       [194, 196, 197, 198, 200, 199, 198, 197, 196, 195],
       [196, 198, 200, 197, 188, 202, 202, 200, 199, 198],
       [199, 201, 207, 168, 130, 193, 198, 201, 202, 202],
       [202, 207, 208, 122, 116, 155, 171, 155, 177, 190],
       [211, 190, 130, 102, 111, 94, 75, 80, 136, 125],
       [161, 143, 66, 86, 93, 85, 65, 73, 125, 94],
       [123, 105, 64, 81, 89, 82, 63, 74, 131, 109],
       [135, 84, 67, 78, 87, 81, 63, 73, 124, 116]]

# Convert the data to a NumPy array
arr = np.array(arr)

# Flatten the data into a 1D array
flat_arr = arr.flatten()

# Calculate the histogram
hist, bins = np.histogram(flat_arr, bins=range(120, 213))  # Adjust the range as needed

# Calculate the cumulative histogram
cumulative_hist = np.cumsum(hist)

# Normalize the cumulative histogram to the range [0, 255]
normalized_cumulative_hist = (cumulative_hist - cumulative_hist.min()) * 255 / (cumulative_hist.max() - cumulative_hist.min())

# Create the equalized image
equalized_image = np.interp(flat_arr, bins[:-1], normalized_cumulative_hist).reshape(arr.shape).astype(np.uint8)

# Create x values that match the length of normalized_cumulative_hist
x_values = np.arange(120, 212)  # Adjust the range to match the length

# Create a plot showing the mapping of input intensities to transformed intensities
plt.figure(figsize=(10, 5))
plt.plot(x_values, normalized_cumulative_hist, '-o', markersize=3, label='Mapping Function')
plt.xlabel('Input Intensity')
plt.ylabel('Transformed Intensity')
plt.title('Mapping of Input Intensities to Transformed Intensities (Equalization)')
plt.legend()
plt.grid()

plt.show()
