import time
import pyperclip
from startup import *
from functions import *

def clipboardUpdate(port):
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            # print("Value changed: " + str(recent_value))
            saveCode(recent_value)
            loadFile(port)
        time.sleep(0.5)

def main():
    # clipboardUpdateThread = threading.Thread(target=clipboardUpdate, daemon=True)
    # clipboardUpdateThread.start()
    
    # subprocess.run(["ampy", "-p COM3", "put"])

    port = startup()
    print(port)
    clipboardUpdate(port)


if __name__ == '__main__':
    main()