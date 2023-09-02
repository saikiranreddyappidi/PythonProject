import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram_equalization(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    cumulative_hist = np.cumsum(hist)
    cumulative_hist_normalized = (cumulative_hist / cumulative_hist[-1]) * 255
    equalized_image = cv2.LUT(image, cumulative_hist_normalized.astype(np.uint8))
    return hist, cumulative_hist, equalized_image


def plot_histograms(hist, cumulative_hist):
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.bar(range(256), hist[:, 0], color='black', width=1.0)
    plt.title("Histogram of Input Image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.subplot(132)
    plt.bar(range(256), cumulative_hist, color='black', width=1.0)
    plt.title("Cumulative Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Cumulative Frequency")

    plt.tight_layout()
    plt.show()


def main():
    input_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original Image", input_image)
    hist, cumulative_hist, equalized_image = histogram_equalization(input_image)
    plot_histograms(hist, cumulative_hist)
    cv2.imshow("Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
