import pyautogui
import cv2

def start(loop=False):
    count = 0
    image = cv2.imread("Images/reactiontime.png")

    while count < 5 or loop:
        if (location := pyautogui.locateOnScreen(image, grayscale=True)) is not None:
            pyautogui.click(location)
            # Clicking one more time to start new test
            pyautogui.click(location)
            print(f"[{count}] Found and clicked...")
            count += 1