import time
import threading
import pyperclip
import subprocess

def clipboardUpdate():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            # print("Value changed: " + str(recent_value))
            saveCode(recent_value)
        time.sleep(0.5)

def loadFile():
    processName = ["ampy"]
    processName.append("-p COM3")
    processName.append("put")

def saveCode(clipboard):
    data = clipboard.split("\n")
    print(data)

def main():
    # clipboardUpdateThread = threading.Thread(target=clipboardUpdate, daemon=True)
    # clipboardUpdateThread.start()
    clipboardUpdate()
    # subprocess.run(["ampy", "-p COM3", "put"])


if __name__ == '__main__':
    main()