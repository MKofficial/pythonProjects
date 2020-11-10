import numpy as np
from PIL import Image


def load(path):
    img = Image.open(path)
    img = img.convert('L')
    return np.array(img).tolist()


def save(image, path):
    if image is None:
        print("Vas obrazek je: None")
        return
    im = _toimg(image)
    im.save(path)


def show(image):
    if image is None:
        print("Vas obrazek je: None")
        return
    im = _toimg(image)
    im.show()


def _toimg(image):
    if image is None:
        print("Vas obrazek je: None")
        return
    arr = np.uint8(np.asarray(image))
    im = Image.fromarray(arr)
    return im
