import os
# import serial.tools.list_ports
# print(list(serial.tools.list_ports.comports()))
import requests


def startup():
    print("Đang kiểm tra dữ liệu cần thiết...")
    firstTime = False
    if not os.path.exists("C:/LongDev"):
        print("Khởi tạo dữ liệu...")
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

    # if not os.path.exists("C:/LongDev/easycode-ampy-bridge/icon.ico"):
    #     print("Đang tải icon...")
    #     response = requests.get("https://longz3r.github.io/icon.ico")
    #     open("C:/LongDev/easycode-ampy-bridge/icon.ico", "wb").write(response.content)

    if not os.path.exists("C:/LongDev/easycode-ampy-bridge/ampy.exe"):
        print("Đang tải ampy...")
        response = requests.get("https://longz3r.github.io/ampy.exe")
        open("C:/LongDev/easycode-ampy-bridge/ampy.exe", "wb").write(response.content)


    if firstTime:
        print("KHỞI ĐỘNG LẦN ĐẦU HOÀN TẤT")
    else:
        print("KHỞI ĐỘNG THÀNH CÔNG")
        print("EASYCODE-AMPY BRIDGE v1.4")

    # configFile = "C:/LongDev/easycode-ampy-bridge/"

    # lastPort = 

    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        return port