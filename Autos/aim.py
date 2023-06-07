import pyautogui
import cv2

def start(loop=False):
    count = 0
    image = cv2.imread("Images/aim.png")

    while count < 31 or loop: # 31 includes the very first target
        print(count)
        if (location := pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)) is not None:
            pyautogui.click(location)
            print(f"[{count}] Found and clicked...")
            count += 1