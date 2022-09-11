import cv2
import numpy as np

class Blob:
    x, y, w, h = int, int, int, int

    def __init__(self, start: 'tuple[int,int]', img: np.ndarray):
        blob = Blob.get_blob(start, img)
        self.x, self.y, self.w, self.h = Blob.get_blob_bounds(blob)
    
    def get_blob(pos: 'tuple[int,int]', img: np.ndarray, checked: 'set[tuple[int,int]]'=set()) -> 'list[tuple[int,int]]':
        pixels = []
        for y in range(pos[0]-1, pos[0]+2):
            for x in range(pos[1]-1, pos[1]+2):
                if (y, x) in checked:
                    break
                checked.add((y, x))
                if img.item(y, x) == 0:
                    pixels.append((y, x))
                    pixels += Blob.get_blob((y, x), img, checked=checked)
                
        return pixels
    
    def get_blob_bounds(blob: 'list[tuple[int,int]]') -> 'int, int, int, int':
        left, right = blob[0][1], blob[0][1]
        top, bottom = blob[0][0], blob[0][0]

        for pixel in blob[1:]:
            if pixel[0] < top:
                top = pixel[0]
            elif pixel[0] > bottom:
                bottom = pixel[0]
            if pixel[1] < left:
                left = pixel[1]
            elif pixel[1] > right:
                right = pixel[1]
        
        return left, top, right-left+1, bottom-top+1

def str_to_grid(string: str):
    return [[letter for letter in row] for row in string.split("\n")]

def img_to_grid(img): # grayscale image
    pass

def test():
    # read image as grayscale
    img = cv2.imread("test_data/cropped_word_search.png", cv2.IMREAD_COLOR)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # convert to binary image
    (thresh, bin_img) = cv2.threshold(grayscale, 128, 256, cv2.THRESH_BINARY)
    # display binary image
    cv2.imshow("binary image", bin_img)
    # find the first blob
    print(bin_img.shape)
    print(bin_img.item(0, 0))
    # crop (19, 11) to (30, 29)
    blob: Blob
    for y in range(bin_img.shape[0]):
        for x in range(bin_img.shape[1]):
            if bin_img.item(y, x) == 0:
                blob = Blob((y, x), bin_img)
                break
        else:
            continue
        break
    print(blob.x, blob.y)
    blobs_img = cv2.rectangle(img, (blob.x, blob.y), (blob.x+blob.w, blob.y+blob.h), (255, 0, 0), thickness=1)
    cv2.imshow("blobs image", blobs_img)
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
    test = Blob((0,2), np_test)
    print(test.x, test.y, test.w, test.h)

print(test())