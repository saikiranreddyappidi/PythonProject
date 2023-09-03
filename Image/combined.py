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


def histogram():
    plt.bar(bins[:-1], hist, width=1, align='edge')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Given Image')
    plt.show()


def cumu_histogram():
    plt.bar(bins[:-1], cumulative_hist, width=1, align='edge')
    plt.xlabel('Value')
    plt.ylabel('Cumulative Frequency')
    plt.title('Cumulative Histogram of Given Image')
    plt.show()


def equalized():
    normalized_cumulative_hist = (cumulative_hist - cumulative_hist.min()) * 255 / (
                cumulative_hist.max() - cumulative_hist.min())
    equalized_image = np.interp(flat_arr, bins[:-1], normalized_cumulative_hist).reshape(arr.shape).astype(np.uint8)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(arr, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')
    plt.show()


def mapping():
    normalized_cumulative_hist = (cumulative_hist - cumulative_hist.min()) * 255 / (
                cumulative_hist.max() - cumulative_hist.min())
    np.interp(flat_arr, bins[:-1], normalized_cumulative_hist).reshape(arr.shape).astype(np.uint8)
    x_values = np.arange(120, 212)
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, normalized_cumulative_hist, '-o', markersize=3, label='Mapping Function')
    plt.xlabel('Input Intensity')
    plt.ylabel('Transformed Intensity')
    plt.title('Mapping of Input Intensities to Transformed Intensities (Equalization)')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    arr = np.array(arr)
    flat_arr = arr.flatten()
    hist, bins = np.histogram(flat_arr, bins=range(120, 213))
    cumulative_hist = np.cumsum(hist)
    histogram()
    cumu_histogram()
    equalized()
    mapping()