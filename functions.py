def saveCode(clipboard):
    # showNotification("Dang luu code")
    data = clipboard.splitlines()
    # data[-1]+="\n"
    
    deleteData = open("C:/LongDev/easycode-ampy-bridge/main.py", "w+")
    deleteData.close()
    file = open("C:/LongDev/easycode-ampy-bridge/main.py", "a")
    for line in data:
        file.write(line+"\n")
    file.close()

from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
notify = ToastNotifier()
  
def showNotification(message, duration=1):
    notify.show_toast("Long Code", message, duration = duration,icon_path ="C:/LongDev/easycode-ampy-bridge/icon.ico")

import subprocess
import serial
import time

def loadFile(port):
    showNotification("Đang nạp code")
    processName = ["cmd"]
    processName.append("/c C:/LongDev/easycode-ampy-bridge/ampy.exe -p " + port +" put C:/LongDev/easycode-ampy-bridge/main.py")

    process = subprocess.run(processName, capture_output=True)
    output = process.stdout.decode()
    print(output)
    showNotification("Đang chạy code")
    # Python code transmits a byte to Arduino /Microcontroller
    SerialObj = serial.Serial(port) # COMxx   format on Windows

    SerialObj.baudrate = 115200  # set Baud rate to 9600
    SerialObj.bytesize = 8     # Number of data bits = 8
    SerialObj.parity   ='N'    # No parity
    SerialObj.stopbits = 1     # Number of Stop bits = 1


    SerialObj.write(b'\x03') #send ctrl-c
    # time.sleep(0.5)
    SerialObj.write(b'\x04')  #send ctrl-d to reset    #transmit 'A' (8bit) to micro/Arduino

    SerialObj.close()          # Close the port
