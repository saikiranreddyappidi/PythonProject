import pandas as pd
import matplotlib.pyplot as plt

# Sample data points
time=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
bandwidth_1 = [63, 77, 124, 124, 124, 63, 77, 124, 124, 124, 124, 129, 833, 833, 833, 833, 833, 833,
                    833, 833, 833, 833, 833, 833, 37, 74, 129, 129, 129, 129, 129, 129, 129, 129, 129, 129,
                    129, 129, 129, 369, 369, 369, 63, 77, 369, 369, 369, 369,369,129]
print(len(time), len(bandwidth_1))
data = {
    'Time': time,
    'Bandwidth-1': bandwidth_1
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the differences between adjacent points
df['Bandwidth-1_diff'] = df['Bandwidth-1'].diff()

# Plot the Bandwidth-1 values
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Bandwidth-1'], marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Bandwidth-1')
plt.title('Graph of Bandwidth-1')
plt.grid(True)
plt.show()

# Print the DataFrame with differences between adjacent points
print(df)
