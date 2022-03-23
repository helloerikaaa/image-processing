import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, *(os.path.pardir,) * 3))
IMAGES_PATH = os.path.join(PROJECT_PATH, 'images')


class Paths:
    original_imgs_path = os.path.join(IMAGES_PATH, 'original')
    generated_imgs_path = os.path.join(IMAGES_PATH, 'generated')
