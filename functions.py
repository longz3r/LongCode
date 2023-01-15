def saveCode(clipboard):
    showNotification("Da")
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
    showNotification("Dang nap code")
    processName = ["mpfshell", "-n", "-c"]
    processName[-1] = "open "+port+ "; put C:/LongDev/easycode-ampy-bridge/main.py main.py"

    process = subprocess.run(processName, capture_output=True)
    output = process.stdout.decode()
    print(output)
    if ("Connected to esp32" in output):
        showNotification("Nap code thanh cong")
    else:
        showNotification(output)
