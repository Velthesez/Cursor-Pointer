import pyautogui
from pynput import keyboard

cursor_position = None


def on_press(key):
     global cursor_position


     if key == keyboard.Key.esc:
          return False
     
     if key.char == 'g':
          cursor_position = pyautogui.position()
          print(f"Cursor: {cursor_position}")

with keyboard.Listener(on_press=on_press) as listener:
     listener.join()