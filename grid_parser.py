import cv2
import numpy as np

class Blob:
    x, y, w, h = int, int, int, int
    
    def get_blob(self, pos: 'tuple[int,int]', img: np.ndarray, checked: 'set[tuple[int,int]]'=set()) -> 'list[tuple[int,int]]':
        pixels = []
        for y in range(pos[0]-1, pos[0]+2):
            for x in range(pos[1]-1, pos[1]+2):
                if (y, x) in checked:
                    break
                checked.add((y, x))
                if img.item(y, x):
                    pixels.append((y, x))
                    pixels += self.get_blob((y, x), img, checked=checked)
                
        return pixels

def str_to_grid(string: str):
    return [[letter for letter in row] for row in string.split("\n")]

def img_to_grid(img): # grayscale image
    pass

def test():
    # read image as grayscale
    img = cv2.imread("test_data/cropped_word_search.png", cv2.IMREAD_GRAYSCALE)
    # convert to binary image
    (thresh, bin_img) = cv2.threshold(img, 128, 256, cv2.THRESH_BINARY)
    print(type(bin_img))
    # display binary image
    cv2.imshow("test", bin_img)
    cv2.waitKey(0)

def blob_test():
    test_arr = [
        [False, False, True, True, False],
        [False, False, True, True, False],
        [False, False, False, True, False],
        [False, True, True, True, False],
        [False, False, False, False, False]
    ]
    np_test = np.array(test_arr)
    print(np_test)
    print(np_test.item((3,1)))
    test = Blob().get_blob((0,2), np_test)
    print(test)

blob_test()