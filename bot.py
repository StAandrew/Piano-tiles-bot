import mss
import pyautogui
from pynput.mouse import Button, Controller
import keyboard
import time

from PIL import Image
from mss import screenshot

blue = [(54, 159, 198)]
black = [(0, 0, 0), (16, 20, 19)]
searchFor = blue

time.sleep(1)
sct = mss.mss()
screenDimensions = {"top": 125, "left": 158, "width": 532, "height": 5}
# screenDimensions = {"top": 124, "left": 158, "width": 530, "height": 685}

# sct_img = sct.grab(screenDimensions)
# img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # Convert to PIL.Image
# img.show()
# exit(0)
status = ""
mouse = Controller()
changed = False
start = time.time()
num = 1
top = 0

while True:
    if keyboard.is_pressed('q'):  # Emergency Button
        break
    # Get a screen shot
    sct_img = sct.grab(screenDimensions)
    searchWidth = sct_img.width

    for i in range(0, searchWidth):
        color = sct_img.pixel(i, 0)
        if 226 < color[0] < 256 and 50 < color[1] < 180 and 60 < color[2] < 160:
            if status != "red":
                status = "red"
                changed = True
                # print(color)
            break
        elif 50 < color[0] < 116 and 80 < color[1] < 204 and 150 < color[2] < 250:
            if status != "blue":
                status = "blue"
                changed = True
                # print(color)
            break
        elif 100 < color[0] < 225 and 70 < color[1] < 186 and 150 < color[2] < 220:
            if status != "purple":
                status = "purple"
                changed = True
                # print(color)
            break
        elif 95 < color[0] < 195 and 185 < color[1] < 230 and 95 < color[2] < 210:
            if status != "green":
                status = "green"
                changed = True
                # print(color)
            break
    if changed:
        if num < 2000:
            add = int(round(0.05*(time.time() - start)))
            top = 10 + add
        elif num > 12420:
            exit(0)
        print(num)
        if status == "blue":
            # print("blue")
            pyautogui.moveTo(220, 124 + top)
            mouse.click(Button.left)
            changed = False
            # cursor.click(220, 560)
        elif status == "purple":
            # print("purple")
            pyautogui.moveTo(350, 124 + top)
            mouse.click(Button.left)
            changed = False
            # cursor.click(350, 560)
        elif status == "red":
            # print("red")
            pyautogui.moveTo(490, 124 + top)
            mouse.click(Button.left)
            changed = False
            # cursor.click(490, 560)
        elif status == "green":
            # print("green")
            pyautogui.moveTo(600, 124 + top)
            mouse.click(Button.left)
            changed = False
            # cursor.click(626, 560)
        num += 1
