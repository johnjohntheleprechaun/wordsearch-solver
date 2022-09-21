import cv2
import numpy as np

class Blob:
    x, y, w, h = int, int, int, int
    pixels: 'set[tuple[int,int]]'
    letter: str

    def __init__(self, start: 'tuple[int,int]', img: np.ndarray):
        blob = Blob.get_blob(start, img, debug=img)
        self.pixels = set(blob)
        self.x, self.y, self.w, self.h = Blob.get_blob_bounds(blob)
        # Create image from pixels
        padded = np.full((self.h+10, self.w+10), 255, dtype=np.uint8)
        for pixel in self.pixels:
            padded.itemset(pixel[0]-self.y+5, pixel[1]-self.x+5, 0)
    
    def get_blob(pos: 'tuple[int,int]', img: np.ndarray, checked: 'set[tuple[int,int]]'=set(), debug=None) -> 'list[tuple[int,int]]':
        pixels = []
        for y in range(pos[0]-1, pos[0]+2):
            for x in range(pos[1]-1, pos[1]+2):
                if (y, x) in checked:
                    continue
                
                checked.add((y, x))

                if img.item(y, x) == 0:
                    pixels.append((y, x))
                    
                    pixels += Blob.get_blob((y, x), img, checked=checked, debug=debug)

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

def img_to_grid(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (tresh, binary) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    blobs = get_blobs(binary)
    grid = []
    row = []
    row_height = blobs[0].h
    current_row = blobs[0].y
    for blob in blobs:
        if abs(blob.y - current_row) > row_height:
            grid.append(row)
            row = []
            current_row = blob.y
        row.append(blob.letter)
    return grid

def get_blobs(img): # binary image
    blobs: 'list[Blob]' = []
    found_pixels: 'set[tuple[int,int]]'= set()
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img.item(y, x) == 0 and not (y, x) in found_pixels:
                blob = Blob((y, x), img)
                blobs.append(blob)
                found_pixels.update(blob.pixels)
    return blobs

def compare_imgs(img1: np.ndarray, img2: np.ndarray):
    return

def average_hash(img):
    resized = cv2.resize(img, (8, 8))
    grayscale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    mean = np.mean(grayscale)
    (thresh, binary) = cv2.threshold(grayscale, mean, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite("out.png", binary)


def test():
    # read image as grayscale
    img = cv2.imread("test_data/image.jpg", cv2.IMREAD_COLOR)
    return average_hash(img)
    

print(test())