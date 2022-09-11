import cv2
import numpy
def str_to_grid(string: str):
    return [[letter for letter in row] for row in string.split("\n")]

def img_to_grid(img): # grayscale image
    pass


def test():
    img = cv2.imread("test_data/cropped_word_search.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("test", img)
    print(img_to_grid(img))
    cv2.waitKey(0)
    pass
test()