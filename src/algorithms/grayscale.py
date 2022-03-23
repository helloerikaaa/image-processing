import numpy as np
from src.utils.image import ImageUtils


def avg_grayscale(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = int(image[i][j][0])
            green = int(image[i][j][1])
            blue = int(image[i][j][2])

            gray_image[i][j] = (red + green + blue) / 3

    return gray_image


def luma_grayscale(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = image[i][j][0]
            green = image[i][j][1]
            blue = image[i][j][2]

            gray_image[i][j] = (red * 0.299) + \
                (green * 0.587) + (blue * 0.114)

    return gray_image


def desaturate(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = int(image[i][j][0])
            green = int(image[i][j][1])
            blue = int(image[i][j][2])

            gray_image[i][j] = (max(red, green, blue) +
                                min(red, green, blue)) / 2

    return gray_image


def max_decomposition(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = int(image[i][j][0])
            green = int(image[i][j][1])
            blue = int(image[i][j][2])

            gray_image[i][j] = max(red, green, blue)

    return gray_image


def min_decomposition(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = int(image[i][j][0])
            green = int(image[i][j][1])
            blue = int(image[i][j][2])

            gray_image[i][j] = min(red, green, blue)

    return gray_image


def red_reduction(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            red = int(image[i][j][0])

            gray_image[i][j] = red

    return gray_image


def green_reduction(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            green = int(image[i][j][1])

            gray_image[i][j] = green

    return gray_image


def blue_reduction(image):
    height, width = ImageUtils().get_image_dimensions(image)
    gray_image = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            blue = int(image[i][j][2])

            gray_image[i][j] = blue

    return gray_image
