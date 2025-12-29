
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

class ImageProcessor:
    def load(self, url):
        try:
            img = Image.open(url)
        except FileNotFoundError as e:
                print("Exception:", e.__class__.__name__, "-- stderr: No such file or directory", file=sys.stderr, sep=" ")
                return None
        except Exception as e:
            print("Exception: OSError -- stderr: None", file=sys.stderr, sep=" ")
            return None
        img_arr = np.asarray(img, dtype=np.float32) /255.0
        print(f'Loading image of demistions {img_arr.shape[0]} X {img_arr.shape[1]}')
        return img_arr
        
    def display(self, array):
        if array is None:
            print(None)
        plt.imshow(array)
        plt.axis("off")
        plt.show()
if __name__ == "__main__":
    new_img = ImageProcessor()
    print(new_img.load("../42AI.png"))
    new_img.display(new_img.load("../42AI.png"))


        