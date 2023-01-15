import subprocess
import threading
import time

def runProcess():
    processName = ["mpfshell", "-n", "-c", 'open COM5; put C:/LongDev/easycode-ampy-bridge/main.py main.py']
    # print(processName[-1])

    # showNotifcation("Dang nap code...",1)
    process = subprocess.run(processName, capture_output=True)
    output = process.stdout.decode()
    output = output.splitlines()
    print(output)

def loadFile(port):
    for i in range(1, 10):
        runProcess()

loadFile("COM3")