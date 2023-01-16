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

def loadFile(port):
    showNotification("Đang nạp code")
    processName = ["cmd"]
    processName.append("/c C:/LongDev/easycode-ampy-bridge/ampy.exe -p " + port +" put C:/LongDev/easycode-ampy-bridge/main.py")

    process = subprocess.run(processName, capture_output=True)
    output = process.stdout.decode()
    print(output)
    showNotification("Đã nạp code")
