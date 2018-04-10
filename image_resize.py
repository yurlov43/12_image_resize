import argparse
import os.path
import sys
from PIL import Image


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='The path to the image')
    parser.add_argument(
        '-w', '--width', type=int,
        help='New image width')
    parser.add_argument(
        '-H', '--height', type=int,
        help='New image height')
    parser.add_argument(
        '-s', '--scale', type=float,
        help='Image change scale')
    parser.add_argument(
        '-out', '--output',
        help='Path to result')
    return parser


def get_path_to_result(path_to_original, new_width, new_height):
    directory, full_filename = os.path.split(path_to_original)
    filename, extension = os.path.splitext(full_filename)
    path_to_result = '{}{}_{}x{}{}'.format(
        directory, filename, new_width, new_height, extension)
    return path_to_result


if __name__ == '__main__':
    parser = get_parser()
    arguments = parser.parse_args()
    path_to_original = arguments.filepath
    path_to_result = arguments.output
    new_width = arguments.width
    new_height = arguments.height
    scale = arguments.scale
    if (new_width or new_height) and scale:
        parser.error('Указаны одновременно стороны изображения и масштаб!')
    image = Image.open(path_to_original)
    image_width, image_height = image.size
    aspect_ratio = round(image_width/image_height, 2)
    if scale:
        new_width = int(image_width*scale)
        new_height = int(image_height*scale)
    elif new_width and new_height:
        if round(new_width/new_height, 2) != aspect_ratio:
            print('Предупреждение: пропорции сторон не соблюдаются!')
    elif new_width:
        new_height = int(new_width/aspect_ratio)
    elif new_height:
        new_width = int(new_height*aspect_ratio)
    new_image = image.resize((new_width, new_height))
    if not path_to_result:
        path_to_result = get_path_to_result(
            path_to_original, new_width, new_height)
    new_image.save(path_to_result)
