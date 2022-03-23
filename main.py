import os
import argparse

from src.utils.image import ImageUtils
from src.consts.paths import Paths
from src.consts.consts import Filters
import pipeline


def main(args):
    image = ImageUtils().open_image(os.path.join(
        Paths.original_imgs_path, args.image_name))
    generated_image = pipeline.FILTERS[args.filter](image)

    if args.save:
        print('Saving image...')
        ImageUtils().save_image(generated_image, os.path.join(
            Paths.generated_imgs_path, args.image_name))
    else:
        print('Showing image...')
        generated_image = ImageUtils().array_to_image(generated_image)
        generated_image.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_name', type=str,
                        help='Name of the image to be manipulated')
    parser.add_argument('filter', type=Filters, choices=list(Filters))
    parser.add_argument('--save', type=bool, default=False,)
    args = parser.parse_args()

    assert args.filter in list(Filters)

    print(f'Starting to process image with {args.filter} filter')

    main(args)
