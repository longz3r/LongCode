import subprocess
import threading
import time

processName = ["mpfshell", "-n", "-c"]
processName[-1] = "open "+"port"+ "; put C:/LongDev/easycode-ampy-bridge/main.py main.py"
print(processName)

# def runProcess():
#     processName = ["mpfshell", "-n -c"]
#     print(processName)

#     # showNotifcation("Dang nap code...",1)
#     process = subprocess.run(processName, capture_output=True)
#     output = process.stdout.decode()
#     print(process.returncode)
#     # output = output.splitlines()
#     print(output)

# from subprocess import Popen, PIPE

subprocess.call(["cmd", "/k C:/LongDev/easycode-ampy-bridge/ampy.exe -p COM3 put C:/LongDev/easycode-ampy-bridge/main.py"])

# print(stdout)

# def loadFile(port):
#     for i in range(1, 10):
#         runProcess()

# loadFile("COM3")

# runProcess()