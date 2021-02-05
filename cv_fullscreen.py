import cv2
import pyautogui
import numpy as np

# vars
screen_name = 'screen'
ix = -1;
iy = -1;
drawing = False
start_x = -1
finish_x = -1
start_y = -1
finish_y = -1
screen = pyautogui.screenshot()
img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

def draw_text(text, img):
    cv2.putText(img, text, (int(img.shape[1] / 2 - 220), 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))


def draw_rectangle(event, x, y, flag, param):
    global img, ix, iy, drawing, start_x, start_y, finish_x, finish_y
    if cv2.EVENT_LBUTTONDOWN == event:
        drawing = True
        ix = x
        iy = y
        start_x = x
        start_y = y
    elif cv2.EVENT_MOUSEMOVE == event:
        if drawing == True:
            img_temp = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)  # img.copy()
            cv2.rectangle(img=img_temp, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=1)
            img = img_temp
    elif cv2.EVENT_LBUTTONUP == event:
        drawing = False
        img_temp = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)  # img.copy()
        cv2.rectangle(img=img_temp, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=1)
        img = img_temp
        finish_x = x
        finish_y = y
        draw_text('Press Esc to commit', img)


def get_coordinates():
    if (start_x, start_y, finish_x, finish_y) == (-1, -1, -1, -1):
        start()
    return (start_x, start_y, finish_x, finish_y)


def start():
    print(img.shape)
    draw_text('Select region', img)
    cv2.namedWindow(screen_name, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(screen_name, draw_rectangle)
    cv2.setWindowProperty(screen_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        cv2.imshow(screen_name, img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    get_coordinates()