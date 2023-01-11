import os
# import serial.tools.list_ports
# print(list(serial.tools.list_ports.comports()))
import requests


def startup():
    firstTime = False
    if not os.path.exists("C:/LongDev"):
        os.mkdir("C:/LongDev")
        firstTime = True
    if not os.path.exists("C:/LongDev/easycode-ampy-bridge"):
        firstTime = True
        os.mkdir("C:/LongDev/easycode-ampy-bridge")
    if not os.path.exists("C:/LongDev/easycode-ampy-bridge/main.py") or not os.path.exists("C:/LongDev/easycode-ampy-bridge/main.py"):
        createFile = open("C:/LongDev/easycode-ampy-bridge/main.py", 'w')
        createFile.close()

        # createFile = open("C:/LongDev/easycode-ampy-bridge/config.txt", 'w')
        # createFile.close()
        
        firstTime = True

    if not os.path.exists("C:/LongDev/easycode-ampy-bridge/icon.ico"):
        response = requests.get("https://longz3r.github.io/icon.ico")
        open("C:/LongDev/easycode-ampy-bridge/icon.ico", "wb").write(response.content)


    if firstTime:
        print("KHOI DONG LAN DAU THANH CONG")
    else:
        print("KHOI DONG THANH CONG")

    # configFile = "C:/LongDev/easycode-ampy-bridge/"

    # lastPort = 

    port = input("NHAP CONG COM (COM3, COM4, COM5) ")
    if len(port) == 4 and port.startswith("COM"):
        pass
    elif len(port) == 1:
        port = "COM" + port
    else:
        print("INVALID PORT")

    return port