import pyautogui
import time

extensions = ("clangd", "C++ TestMate", "C++ Helper", "Cmake", "CMake Tools")

time.sleep(3)

pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(3)
pyautogui.typewrite("code .")
time.sleep(3)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(3)

extX, extY = pyautogui.locateCenterOnScreen("ext.png")
pyautogui.click(extX, extY, 1, 2, button="left")
time.sleep(2)
pyautogui.moveRel(70, -200)
pyautogui.leftClick()
pyautogui.hotkey('shift', 'del')
time.sleep(2)

for extension in extensions:
    pyautogui.typewrite(extension)
    time.sleep(20)
    pyautogui.moveRel(0, 50)
    pyautogui.leftClick()
    time.sleep(2)
    try:
        installX, installY = pyautogui.locateCenterOnScreen("install.png")
    except pyautogui.ImageNotFoundException:
        installX, installY = pyautogui.locateCenterOnScreen("install2.png")
    pyautogui.click(installX, installY, 1, 2, button="left")
    time.sleep(5)
    clearX, clearY = pyautogui.locateCenterOnScreen("clear.png")
    pyautogui.click(clearX, clearY, 1, 2, button="left")
