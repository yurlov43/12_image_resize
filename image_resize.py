import argparse
import os.path
import sys
from PIL import Image


def parser_arguments():
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
    return parser.parse_args()


def analysis_of_arguments(arguments, aspect_ratio=None):
    error_in_arguments = None
    if not os.path.exists(arguments.filepath):
        error_in_arguments = 'Ошибка: файл не найден!'
    elif((arguments.width or arguments.height) and arguments.scale):
        error_in_arguments = '''Ошибка:
            указаны одновременно стороны изображения и масштаб!'''
    elif(arguments.width and arguments.height and aspect_ratio):
        if(round(arguments.width/arguments.height, 2) != aspect_ratio):
            error_in_arguments = 'Ошибка: пропорции сторон не соблюдаются!'
    return error_in_arguments


def get_scale(image_width, image_height, new_width, new_height):
    scale = 1
    if new_height:
        scale = new_height/image_height
    elif new_width:
        scale = new_width/image_width
    return scale


def get_path_to_result(path_to_original, new_width, new_height):
    directory, file = os.path.split(path_to_original)
    filename, extension = os.path.splitext(file)
    path_to_result = '{}{}_{}x{}{}'.format(
        directory, filename, new_width, new_height, extension)
    return path_to_result


if __name__ == '__main__':
    arguments = parser_arguments()
    error_in_arguments = analysis_of_arguments(arguments)
    if error_in_arguments:
        sys.exit(error_in_arguments)
    path_to_original = arguments.filepath
    path_to_result = arguments.output
    new_width = arguments.width
    new_height = arguments.height
    scale = arguments.scale
    image = Image.open(path_to_original)
    image_width, image_height = image.size
    aspect_ratio = round(image_width/image_height, 2)
    error_in_arguments = analysis_of_arguments(arguments, aspect_ratio)
    if error_in_arguments:
        sys.exit(error_in_arguments)
    if not scale:
        scale = get_scale(image_width, image_height, new_width, new_height)
    new_width = int(image_width*scale)
    new_height = int(image_height*scale)
    new_image = image.resize((new_width, new_height))
    if not path_to_result:
        path_to_result = get_path_to_result(
            path_to_original, new_width, new_height)
    new_image.save(path_to_result)
