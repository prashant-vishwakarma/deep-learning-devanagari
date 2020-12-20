import cv2
import imageio
import numpy as np


def calc_top(top, img, white, length, height):
    try:
        for x in range(height):
            for y in range(length):
                if not np.array_equal(img[x][y], white):
                    top = x
                    raise StopIteration
    except StopIteration:
        print('Top Calculated: ', top)


def calc_bottom(bottom, white, img, length, height):
    try:
        for x in range(height - 1, -1, -1):
            for y in range(length):
                if not np.array_equal(img[x][y], white):  # here
                    bottom = x
                    raise StopIteration
    except StopIteration:
        print('Bottom Calculated: ', bottom)


def calc_left(left, img, white, length, height):
    try:
        for y in range(length):
            for x in range(height):
                if not np.array_equal(img[x][y], white):  # here
                    left = y
                    raise StopIteration
    except StopIteration:
        print('Left Calculated: ', left)


def calc_right(right, img, white, length, height):
    try:
        for y in range(length - 1, -1, -1):
            for x in range(height):
                if not np.array_equal(img[x][y], white):  # here
                    right = y
                    raise StopIteration
    except StopIteration:
        print('Right Calculated: ', right)


def crop():
    # read image
    img = cv2.imread(r'kamal.png')
    # a x b
    length = img.shape[1]
    height = img.shape[0]
    print('**Image dimensions** ')
    print('\nheight X: ', height, '  length Y: ', length)
    print(img.shape)

    # part2
    white = np.array([255, 255, 255])
    left = 0
    right = length - 1
    top = 0
    bottom = height - 1

    top = calc_top(top, img, white, length, height)

    calc_bottom(bottom, white, img, length, height)

    calc_left(left, img, white, length, height)

    calc_right(right, img, white, length, height)

    # cropped output
    word = img[top:bottom, left:right]
    imageio.imwrite('word_cropped.jpg', word[:, :, 0])
