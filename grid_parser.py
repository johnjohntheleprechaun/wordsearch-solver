import cv2

def str_to_grid(string: str):
    return [[letter for letter in row] for row in string.split("\n")]

def img_to_grid(img): # grayscale image
    pass

def test():
    # read image as grayscale
    img = cv2.imread("test_data/cropped_word_search.png", cv2.IMREAD_GRAYSCALE)
    # convert to binary image
    (thresh, bin_img) = cv2.threshold(img, 128, 256, cv2.THRESH_BINARY)
    # display binary image
    cv2.imshow("test", bin_img)
    cv2.waitKey(0)

test()