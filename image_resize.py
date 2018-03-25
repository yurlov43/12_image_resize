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


def resize_image(argumentst):
    path_to_original = arguments.filepath
    if not os.path.exists(path_to_original):
        sys.exit("Ошибка: файл не найден!")
    path_to_result = arguments.output
    new_width = arguments.width
    new_height = arguments.height
    scale = arguments.scale
    if((new_width or new_height) and scale):
        sys.exit("Ошибка: указаны одновременно стороны изображения и масштаб!")
    image = Image.open(path_to_original)
    image_width = image.size[0]
    image_height = image.size[1]
    if(not scale):
        scale = image_height/image_height
    if(new_height):
        scale = new_height/image_height
        if(new_width and scale != new_width/image_width):
            sys.exit("Ошибка: пропорции сторон не соблюдаются!")
    else:
        if(new_width):
            scale = new_width/image_width
    new_width = int(image_width*scale)
    new_height = int(image_height*scale)
    new_image = image.resize((new_width, new_height))    
    if(not path_to_result):
        directory, file = os.path.split(path_to_original)
        filename, extension = os.path.splitext(file)
        path_to_result = ('{}{}_{}x{}{}'.
            format(directory, filename, new_width, new_height, extension))
    new_image.save(path_to_result)


if __name__ == '__main__':
    arguments = parser_arguments()
    resize_image(arguments)
