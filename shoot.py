import mss
import time
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
import coordinates as kos_co
import numpy as np

# BOX_COORS = {'top':kos_co.get_coors()[0],'left':kos_co.get_coors()[1],''}
BOX_COORS = {'top': 111, 'left': 222, 'width': 34, 'height': 50}


def screen_record():
    sct = mss.mss()
    last_time = time.time()
    while True:
        sct_img = sct.grab(BOX_COORS)

        # print(m)
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', "BGRX")
        draw = ImageDraw.Draw(im=img, mode=img.mode)
        img.save('111.png')
        # img = np.array(img)
