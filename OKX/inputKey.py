import tkinter as tk
import json

# 全局變數
window = None
keyEntry = None
skeyEntry = None
passwdEntry = None
flag = None

# 金鑰輸入視窗
def keyGUI():
    global window, keyEntry, skeyEntry, passwdEntry, flag
    # 建立主視窗
    window = tk.Tk()
    window.title("API載入")
    window.geometry("300x180")

    # API Key(金鑰) 輸入框
    keyLabel = tk.Label(window, text="金鑰:")
    keyLabel.pack(pady = 1)
    keyEntry = tk.Entry(window)
    keyEntry.pack()

    # Secret Key(密鑰) 輸入框
    skeyLabel = tk.Label(window, text="密鑰:")
    skeyLabel.pack(pady = 1)
    skeyEntry = tk.Entry(window, show="*")
    skeyEntry.pack()

    # Password(密碼) 輸入框
    passwdLabel = tk.Label(window, text="密碼:")
    passwdLabel.pack(pady = 1)
    passwdEntry = tk.Entry(window, show="*")
    passwdEntry.pack()

    # 父容器框架(排版按鈕和勾選盒)
    frame = tk.Frame(window)
    frame.pack(side = "bottom", pady = 5)

    # 送出按鈕(子部件)
    submit_button = tk.Button(frame, text="儲存", command=submitKey)
    submit_button.grid(row=0, column=0)

    # 模擬盤勾選框(子部件)
    flag = tk.IntVar()
    checkbox = tk.Checkbutton(frame, text="模擬盤", variable=flag)
    checkbox.grid(row=0, column=1)

    # 啟動主迴圈
    window.mainloop()

# 送出功能
def submitKey():
    global window, keyEntry, skeyEntry, passwdEntry, flag
    # 取得在輸入框裡的內容
    apikey = keyEntry.get()
    secretkey = skeyEntry.get()
    passwd = passwdEntry.get()
    flag = flag.get()
    # 建立字典
    Data = {
        "apikey": apikey,
        "secretkey": secretkey,
        "passwd": passwd,
        "flag" : flag
    }

    # 將資料儲存為 JSON 格式
    with open("keydata.json", "w") as f:
        json.dump(Data, f)

    # 關閉視窗
    window.destroy()

keyGUI()