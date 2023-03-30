import time
import pyperclip
from startup import *
from functions import *
import keyboard
import pyautogui

from win32api import GetSystemMetrics

def clipboardUpdate(port):
    recent_value = pyperclip.paste()
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            # print("Value changed: " + str(recent_value))
            if recent_value.startswith("import") or recent_value.startswith('from'):
                saveCode(recent_value)
                loadFile(port)
        time.sleep(0.5)

def keyboardUpdate(port):
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed("F5"):
            pyautogui.press("enter")
            with pyautogui.hold("ctrl"):
                pyautogui.press(["a", "c"])
            saveCode(pyperclip.paste())
            loadFile(port)


def main():
    # clipboardUpdateThread = threading.Thread(target=clipboardUpdate, daemon=True)
    # clipboardUpdateThread.start()
    
    # subprocess.run(["ampy", "-p COM3", "put"])

    port = startup()
    if port != None:
        print("Đã kết nối đến cổng " + str(port))
        print("Sẵn sàng")
        if GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768:
            print("One button run enabled")
            print("make sure easycode is maximized")
            keyboardUpdate(str(port))
        else:
            clipboardUpdate(str(port))
    elif port == None:
        print("Không thể tìm thấy cổng serial nào")
        print("Nếu thiết bị đã được kết nối hãy thử cài đặt lại driver trong easycode")
        print("Tự động đóng chương trình trong 10s")
        time.sleep(10)
    else:
        print("LỖI ĐÉO AI BIẾT")


if __name__ == '__main__':
    main()