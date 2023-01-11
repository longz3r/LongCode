import time
import threading
import pyperclip
import subprocess
import os

config = {
    
}

def clipboardUpdate():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            # print("Value changed: " + str(recent_value))
            saveCode(recent_value)
        time.sleep(0.5)

def startup():
    firstTime = False
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
        firstTime = True
    if not os.path.exists("C:/LongDev/easycode-ampy-bridge"):
        firstTime = True
        os.mkdir("C:/LongDev/easycode-ampy-bridge")
    if not os.path.exists("C:/LongDev/easycode-ampy-bridge/main.py"):
        createFile = open("C:/LongDev/easycode-ampy-bridge/main.py", 'w')
        createFile.close()
        firstTime = True
    if firstTime:
        print("KHOI DONG LAN DAU THANH CONG")
    else:
        print("KHOI DONG THANH CONG")

    port = input("NHAP CONG COM (COM3, COM4, COM5)")
    config["port"] = port
    print([port])

def loadFile():
    processName = ["ampy"]
    processName.append("-p COM3")
    processName.append("put")

def saveCode(clipboard):
    print("Saving code...")
    data = clipboard.split("\n")
    data[-1]+="\n"
    
    deleteData = open("C:/LongDev/easycode-ampy-bridge/main.py", "w+")
    deleteData.close()
    file = open("C:/LongDev/easycode-ampy-bridge/main.py", "a")
    for line in data:
        file.write(line)
    file.close()

def main():
    # clipboardUpdateThread = threading.Thread(target=clipboardUpdate, daemon=True)
    # clipboardUpdateThread.start()
    
    # subprocess.run(["ampy", "-p COM3", "put"])

    startup()
    clipboardUpdate()


if __name__ == '__main__':
    main()