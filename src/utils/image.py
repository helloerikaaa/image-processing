import numpy as np
from PIL import Image


class ImageUtils:

    def open_image(self, filename):
        image = np.asarray(Image.open(filename))
        return image

    def save_image(self, image, filename):
        image.save(filename)

    def get_image_dimensions(self, image):
        height, width = image.shape[0], image.shape[1]
        return height, width

    def array_to_image(self, array):
        image = Image.fromarray(np.uint8(array))
        return image
