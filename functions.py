def saveCode(clipboard):
    print("Saving code...")
    data = clipboard.splitlines()
    # data[-1]+="\n"
    
    deleteData = open("C:/LongDev/easycode-ampy-bridge/main.py", "w+")
    deleteData.close()
    file = open("C:/LongDev/easycode-ampy-bridge/main.py", "a")
    for line in data:
        file.write(line)
    file.close()

from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
notify = ToastNotifier()
  
def showNotifcation(message, duration=3):
    notify.show_toast("Long Code", message, duration = duration,icon_path ="icon.ico")

import subprocess
import time

def loadFile(port):
    processName = ["ampy"]
    processName.append("-p " + port)
    processName.append("put")
    processName.append("C:/LongDev/easycode-ampy-bridge/main.py")

    showNotifcation("Dang nap code...",1)
    process = subprocess.run(processName, capture_output=True)
    if process.returncode == 0:
        output = process.stdout.decode()
        output = output.splitlines()
        print(output)
    if process.returncode == 1:
        output = process.stderr.decode()
        output = output.splitlines()
        print(output[-1])
        showNotifcation("Lỗi:" + output[-1].split(':')[1])


    
