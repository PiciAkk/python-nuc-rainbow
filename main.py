from os import system as runcmd
from os import startfile as startApp
import subprocess
import os
import time
if os.path.isdir("C:\Program Files (x86)\Intel Corporation\LED Manager for Intel(R) NUC"):
    print("Intel NUC Manager detected. Continuing...")
else:
    print("Intel NUC Manager is not detected. Please install it using the link below.")
    exit
print("Enabling RGB mode...")
rgbColors = ["redSkull", "orangeSkull", "yellowSkull1", "yellowSkull2", "greenSkull1", "greenSkull2", "greenSkull3", "mintSkull", "aquaSkull", "blueSkull1", "blueSkull2", "blueSkull3", "blueSkull4", "purpleSkull1", "purpleSkull2", "pinkSkull1", "pinkSkull2", "pinkSkull3", "pinkRedSkull"]
while True:
    for i in rgbColors:
        subprocess.Popen([r'C:/Program Files (x86)/Intel Corporation/LED Manager for Intel(R) NUC/LEDManagerCLI.exe', '/profile', i])
        time.sleep(0.5)
