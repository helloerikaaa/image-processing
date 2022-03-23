from tqdm import tqdm
import matplotlib.pyplot as plt

from src.utils.image import ImageUtils


def _get_grayscale_hist(image):
    height, width = ImageUtils().get_image_dimensions(image)
    bins = []
    hist_range = range(256)
    for p in tqdm(hist_range):
        value = 0
        for i in range(height):
            for j in range(width):
                if image[i][j] == p:
                    value += 1
        bins.append(value)

    plt.bar(hist_range, bins)
    plt.show()


def _get_color_hist(image):
    height, width = ImageUtils().get_image_dimensions(image)
    red_bins = []
    green_bins = []
    blue_bins = []
    hist_range = range(256)

    for p in tqdm(hist_range):
        red = 0
        green = 0
        blue = 0
        for i in range(height):
            for j in range(width):
                if image[i][j][0] == p:
                    red += 1
                elif image[i][j][1] == p:
                    green += 1
                elif image[i][j][2] == p:
                    blue += 1
        red_bins.append(red)
        green_bins.append(green)
        blue_bins.append(blue)

    plt.plot(hist_range, red_bins, color='red')
    plt.plot(hist_range, green_bins, color='green')
    plt.plot(hist_range, blue_bins, color='blue')

    plt.show()


def get_histogram(image):
    if image.ndim == 2:
        print('Getting histogram of a grayscale image')
        _get_grayscale_hist(image)
    elif image.ndim == 3:
        print('Getting histogram of a color image')
        _get_color_hist(image)
