import pyautogui
import time

try:
    while True:
        pyautogui.hotkey('ctrl', 'v')  # Simulate pressing Ctrl + V
        time.sleep(0.1)  # Short delay to ensure Ctrl + V is processed
        pyautogui.press('enter')  # Simulate pressing Enter
        time.sleep(5)  # Wait for 5 seconds before repeating
except KeyboardInterrupt:
    print("Script stopped by user.")