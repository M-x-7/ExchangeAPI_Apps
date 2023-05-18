import keyboard
import requests
import datetime
import json
import time
import base64
import hmac
import hashlib
import os
import settings

# API連線功能
def apiSet(api_key, secret_key, api_password,request_path):
  # 時間及路徑設置
  method = "GET"                                                          # 請求方法
  timestamp = datetime.datetime.utcnow().isoformat()[:-3]+"Z"             # ISO格式時間戳
  prehash_string = timestamp + method + request_path                      # 合成預置字串

  # 預置字串用密鑰HMAC-SHA256加密，再經過Base64編碼
  signature = base64.b64encode(hmac.new(secret_key.encode(), prehash_string.encode(), hashlib.sha256).digest()).decode()

  # 設置請求頭部信息
  headers = {
    "OK-ACCESS-KEY": api_key,
    "OK-ACCESS-SIGN": signature,
    "OK-ACCESS-TIMESTAMP": timestamp,
    "OK-ACCESS-PASSPHRASE": api_password,
    "Content-Type": "application/json",
  }
  # 發送API請求
  response = requests.get("https://www.okx.com" + request_path, headers=headers)
  # 返回Json格式資料
  
  return response.json()


# 設定預設選項列表和初始化目前選擇的項目
options = ['Balance', 'BTC price', 'ETH price']
current_option = 0

# 導入API金鑰和密鑰
api_key = settings.key
secret_key = settings.skey
api_password = settings.passwd

# 顯示目前選項和其它選項
def show_options():
  for i in range(len(options)):
      if i == current_option:
          print('>> ' + options[i])
      else:
          print('   ' + options[i])
show_options()

#程式迴圈
while True:
  while True:
        try:
            time.sleep(0.15)

            # 按下上方向鍵
            if keyboard.is_pressed('up'):
                os.system('cls')
                if current_option == 0:
                    current_option = 2
                else:
                    current_option -= 1
                show_options()

            # 按下下方向鍵
            elif keyboard.is_pressed('down'):
                os.system('cls')
                if current_option == 2:
                    current_option = 0
                else:
                    current_option += 1
                show_options()

            # 如果按Enter鍵，確認選擇並退出
            elif keyboard.is_pressed('enter'):
                break

        # 捕捉並處理keyboard.interrupt_exception例外
        except keyboard.KeyboardInterrupt:
            break
        



  while True:
    # 路徑隨選擇導入
    path = ''
    if current_option == 0:
      path = settings.paths[0]
    elif current_option == 1:
      path = settings.paths[1]
    elif current_option == 2:
      path = settings.paths[2]

    #調用API，並根據選項輸出內容
    Temp = apiSet(api_key, secret_key, api_password, path)
    if current_option == 0:
        type = "USD Valuation"
        values = Temp["data"][0]["totalEq"][:-10]
    else :
        type = Temp["data"][0]["instId"]
        values = Temp["data"][0]["last"]
    print(type +": " +values)
    break
