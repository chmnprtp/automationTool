import pyautogui
import subprocess
import time

# Replace 'brave' with the actual name of the Brave executable if needed
brave_executable = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'


# Use subprocess to open Brave
subprocess.Popen([brave_executable])

time.sleep(2)

pyautogui.press('\t')
pyautogui.press('enter')
time.sleep(2)

# time.sleep(1)
# pyautogui.press('pagedown')
# time.sleep(2)


pyautogui.hotkey('command', 'r')

time.sleep(3)