import cv2 as cv
import pyautogui
import numpy as np

img = pyautogui.screenshot()
screen = cv.cvtColor(np.array(img),cv.COLOR_RGB2BGR)
cv.imshow('screen',screen)
cv.waitKey()