import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram_equalization(image):
    # Compute the histogram of the input image
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Compute the cumulative histogram
    cumulative_hist = np.cumsum(hist)

    # Normalize the cumulative histogram
    cumulative_hist_normalized = (cumulative_hist / cumulative_hist[-1]) * 255

    # Equalize the image
    equalized_image = cv2.LUT(image, cumulative_hist_normalized.astype(np.uint8))

    return hist, cumulative_hist, equalized_image


def plot_histogram(hist, title="Histogram"):
    plt.figure(figsize=(8, 4))
    plt.bar(np.arange(256), hist.flatten(), color='black', width=1.0)
    plt.title(title)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 255])
    plt.show()


def main():
    # Load the grayscale image (replace 'input_image.jpg' with your image file)
    input_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

    # Perform histogram equalization
    hist, cumulative_hist, equalized_image = histogram_equalization(input_image)

    # Display the histogram and cumulative histogram
    plot_histogram(hist, title="Histogram of Input Image")

    # Display the equalized image
    cv2.imshow("Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
