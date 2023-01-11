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

from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
notify = ToastNotifier()
  
def showNotifcation(message):
    notify.show_toast("Long Code", message, duration = 3,icon_path ="icon.ico")

def loadFile(port):
    processName = ["ampy"]
    processName.append("-p " + port)
    processName.append("put")

    showNotifcation("Dang nap code...")
