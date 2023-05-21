import keyboard
import requests
import datetime
import json
import time
import base64
import hmac
import hashlib

# 檢查keydata內容是否為空
def Check_keydata():
  with open("keydata.json", "r") as f:
    data = json.load(f)
    if not data["apikey"] or not data["secretkey"] or not data["passwd"] or not data["flag"]:
      import inputKey
      inputKey.keyGUI()
    
# 時間戳獲取功能(交易所系統時間)
def sysTime():
  # 從交易所獲取時間
  systemTime = int(requests.get("https://www.okx.com/api/v5/public/time").json()["data"][0]["ts"])
  # 轉換為ISO格式時間戳
  isoTimestamp = datetime.datetime.fromtimestamp(systemTime/1000).isoformat()[:-3]+"Z"        
  return isoTimestamp

# 時間戳獲取功能(UTC標準時間)
def utcTime():
  # 獲取UTC時間
  utcTime = datetime.datetime.utcnow()
  # 轉換為ISO格式時間戳
  isoTimestamp = utcTime.isoformat()[:-3]+"Z"        
  return isoTimestamp

# API連線功能
def apiSet(apikey, secretkey, passwd, path, flag):
  # 時間及路徑設置
  method = "GET"
  timestamp = utcTime()

  # 合成預置字串
  prehashString = timestamp + method + path

  # 預置字串用密鑰HMAC-SHA256加密，再經過Base64編碼
  signature = base64.b64encode(hmac.new(secretkey.encode(), prehashString.encode(), hashlib.sha256).digest()).decode()

  # 設置請求頭部信息
  headers = {
    "OK-ACCESS-KEY": apikey,
    "OK-ACCESS-SIGN": signature,
    "OK-ACCESS-TIMESTAMP": timestamp,
    "OK-ACCESS-PASSPHRASE": passwd,
    "Content-Type": "application/json",
    "x-simulated-trading": flag
  }
  # 發送API請求
  response = requests.get("https://www.okx.com" + path, headers=headers)
  # 返回Json格式資料
  return response.json()

#--------------------
#     主程式開始
#--------------------

# 檢查或導入金鑰
Check_keydata()
with open("keydata.json", "r") as f:
  data = json.load(f)
  apikey = data["apikey"]
  secretkey = data["secretkey"]
  passwd = data["passwd"]
  flag = data["flag"]

# 程式迴圈



