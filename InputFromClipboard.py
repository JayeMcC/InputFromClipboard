import keyboard
import pyperclip

def paste_from_clipboard():
    clipboard_text = pyperclip.paste()
    lines = clipboard_text.split("\n")
    for line in lines:
        keyboard.write(line)
        keyboard.press_and_release("enter")

# Example hotkey binding (Ctrl+Shift+V)
keyboard.add_hotkey('ctrl+shift+v', paste_from_clipboard)

keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit the script
