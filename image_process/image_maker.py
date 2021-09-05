

import numpy as np
from PIL import Image

array = np.array([[255, 0, 255, 255, 255], 
                  [255, 0, 255, 100, 255],
                  [255, 0, 255, 100, 255], 
                  [255, 0, 255, 100, 255], 
                  [255, 0, 255, 100, 255],
                  [255, 0, 255, 100, 255],
                  [255, 0, 255, 255, 255]], dtype=np.uint8)
print(array)

im = Image.fromarray(array)

im.save("image_process/number_img/10.jpg")