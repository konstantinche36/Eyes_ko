import pynput

x_start = 0
y_start = 0
x_finish = 0
y_finish = 0


def on_click(x, y, button, pressed):
    global x_start, y_start, x_finish, y_finish
    if pressed:
        x_start = x
        y_start = y
        print('{0} at {1}'.format(x, y))
        return True
    elif not pressed:
        x_finish = x
        y_finish = y
        print('{0} at {1}'.format(x, y))
        return False


def calc_coors():
    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()


def get_coors():
    if (x_start, y_start, x_finish, y_finish) == (0, 0, 0, 0):
        calc_coors()
    return x_start, y_start, x_finish, y_finish


def reset_coors():
    global x_start, y_start, x_finish, y_finish
    x_start, y_start, x_finish, y_finish = (0, 0, 0, 0)
