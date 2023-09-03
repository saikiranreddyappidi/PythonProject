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

# Flatten the data into a 1D array 
flat_arr = np.array(arr).flatten()

# Calculate the histogram
hist, bins = np.histogram(flat_arr, bins=range(120, 213))  # Adjust the range as needed

# Create a bar graph
plt.bar(bins[:-1], hist, width=1, align='edge')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Given Image')

# Show the plot
plt.show()

