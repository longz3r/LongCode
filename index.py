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
    print(port)
    clipboardUpdate(port)


if __name__ == '__main__':
    main()