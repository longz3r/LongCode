import time
import pyperclip
from startup import *
from functions import *

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

def main():
    # clipboardUpdateThread = threading.Thread(target=clipboardUpdate, daemon=True)
    # clipboardUpdateThread.start()
    
    # subprocess.run(["ampy", "-p COM3", "put"])

    port = startup()
    if port != None:
        print("Đã kết nối đến cổng " + str(port))
        print("Sẵn sàng")
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