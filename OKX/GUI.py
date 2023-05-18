import tkinter as tk
import json

# 全局變數
window = None
keyEntry = None
skeyEntry = None
passwdEntry = None


# 建立視窗功能
def createGUI():
    global window, keyEntry, skeyEntry, passwdEntry
    # 建立主視窗
    window = tk.Tk()
    window.title("API載入")
    window.geometry("400x200")

    # API Key(金鑰) 輸入框
    keyLabel = tk.Label(window, text="金鑰:")
    keyLabel.pack()
    keyEntry = tk.Entry(window)
    keyEntry.pack()

    # Secret Key(密鑰) 輸入框
    skeyLabel = tk.Label(window, text="密鑰:")
    skeyLabel.pack()
    skeyEntry = tk.Entry(window, show="*")
    skeyEntry.pack()

    # Password(密碼) 輸入框
    passwdLabel = tk.Label(window, text="API Password:")
    passwdLabel.pack()
    passwdEntry = tk.Entry(window, show="*")
    passwdEntry.pack()

    # 送出按鈕
    submit_button = tk.Button(window, text="儲存", command=submitKey)
    submit_button.pack()

    # 啟動主迴圈
    window.mainloop()

# 訊息送出功能
def submitKey():
    global window, keyEntry, skeyEntry, passwdEntry
    # 取得在輸入框裡的內容
    apikey = keyEntry.get()
    secretkey = skeyEntry.get()
    passwd = passwdEntry.get()

    # 建立字典
    Data = {
        "apikey": apikey,
        "secretkey": secretkey,
        "passwd": passwd
    }

    # 將資料儲存為 JSON 格式
    with open("keydata.json", "w") as json_file:
        json.dump(Data, json_file)

    # 關閉視窗
    window.destroy()

