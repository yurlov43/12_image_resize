# Image Resizer

The program resizes the image.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux and Windows, Python 3.5:

```bash
$ python image_resize.py filepath -w -H -s -out 
```
```bash
Required parameters:
filepath - The path to the image
Optional parameters:
-w (--width) - New image width
-H (--height) - New image height
-s (--scale) - Image change scale
-out (--output) - Path to result
```

The result is stored in the specified path or saved next to the original image, with the width and height of the image added to the file name.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
