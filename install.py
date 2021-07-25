from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import pyautogui
app = Application().start(r"C:\Program Files (x86)\Intel Corporation\LED Manager for Intel(R) NUC\LEDManagerForIntelNUC.exe")
ledManagerApp = app['LED Manager for Intel® NUC']
ledManagerApp.set_focus()
print(ledManagerApp.get_toolbar())
