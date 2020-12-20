import cv2
import imageio
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from matplotlib import pyplot as plt
from skimage.transform import resize

MODEL_FILE_NAME = 'model_name.h5'


def show_image(input_image):
    # Plots image
    assert len(input_image.shape) == 3, "Image passed in is of incorrect shape"
    plt.imshow(input_image.squeeze())
    plt.show()


def read_dimensions(img):
    # a x b
    length = img.shape[1]
    height = img.shape[0]
    print('\n\n**Cropped image dimension**')
    print('\nheight X: ', height, ' x length Y: ', length)
    return length, height


def run_prediction(model, word):
    word_len = len(word)
    print("\n\n**Char Prediction for word length ", word_len, " **")
    i = 0
    for x in word:
        i += 1
        imageio.imwrite('temp.jpg', x[:, :, 0])
        test_image = image.load_img(r'temp.jpg', target_size=(32, 32))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        print('\n Predicted o/p for char ', i)
        print("\n", result)


def predict():
    # read
    img = cv2.imread(r'word_cropped.jpg')
    length, height = read_dimensions(img)

    # count black pixel occurrence
    black_counter = []
    for x in range(length):
        black_counter.append(0)
    white = np.array([255, 255, 255])

    for y in range(length):
        for x in range(height):
            if not np.array_equal(img[x][y], white):  # here
                black_counter[y] = black_counter[y] + 1
    min_count = min(black_counter)
    print('Min: ', min_count)

    # calculate min
    low = min_count  # - min_count*0.4
    high = 27
    print('low: ', low)
    print('high: ', high)

    # part5
    show_image(img)
    plt.plot(black_counter)

    # part6
    points = []
    flag = False
    for x in range(len(black_counter)):
        if not flag and high > black_counter[x] >= low:
            points.append(x)
            flag = True
        elif black_counter[x] > high:
            flag = False

    # part8
    word = []
    for i in range(len(points)):
        if i != len(points) - 1:
            word.append(img[0:height, points[i]:points[i + 1]])
            show_image(word[i])

    # part1
    word[1] = resize(word[1], (32, 32))

    # part2
    show_image(word[1])

    # load model
    model = load_model(MODEL_FILE_NAME)

    # part4
    run_prediction(model, word)
