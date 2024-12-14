import cv2
import numpy as np
import pyautogui
import time

def find_and_click(image_path):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Load the image to find
    template = cv2.imread(image_path)
    template_height, template_width = template.shape[:2]

    # Perform template matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9  # You can adjust this threshold
    loc = np.where(result >= threshold)

    # If a match is found, click on it
    for pt in zip(*loc[::-1]):  # Switch columns and rows
        # Calculate the center of the detected area
        center_x = pt[0] + template_width // 2
        center_y = pt[1] + template_height // 2
        
        # Move the mouse to the center of the detected image and click
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
        print(f"Clicked at: ({center_x}, {center_y})")
        break  # Remove this if you want to click on all found instances

if __name__ == "__main__":
    image_path = r'C:\Users\salmi\OneDrive\Desktop\safjh\yus.png'  # Replace with your image path
    while True:
        find_and_click(image_path)
        time.sleep(0)  # Adjust the sleep time as needed