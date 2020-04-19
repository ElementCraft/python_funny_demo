# encoding:utf-8
import requests
import time
import base64
import tkinter
import tkinter.filedialog
import tkinter.font
import os

CLIENT_KEY = "RxN6WghA0xQt2lu7G1B95UAH"
CLIENT_SECRET = "9YIRb9FFT9zGWpZITWg6ivBdrA1SQ6rI"
API_GET_ACCESS_TOKEN = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
API_OCR_GENERAL_BASIC = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s"

file_path = ""

access_token = ""
refresh_token = ""
expired_in = 0

tk = None

result_words = []

def getAccessToken():
    global access_token, refresh_token, expired_in
    now = time.time()
    if(now < expired_in and len(access_token) > 0):
        return access_token

    url = API_GET_ACCESS_TOKEN % (CLIENT_KEY, CLIENT_SECRET)
    response = requests.get(url)
    if response:
        data = response.json()
        access_token = data["access_token"]
        refresh_token = data["refresh_token"]
        expired_in = now + float(data["expires_in"])
        #print(access_token, expired_in)
        return access_token
    else:
        raise Exception("[error]请求数据失败，请检查网络")

def init():
    global tk
    tk = tkinter.Tk()
    tk.title('OCR识别')
    tk.geometry("480x320+200+100")
    #tk.resizable(width=False,height=False)
    

def showResult():
    global tk
    if tk == None:
        raise Exception("[error]请先选择要识别的图片")

    ft = tkinter.font.Font(family="微软雅黑", size=20)
    lt = tkinter.Listbox(tk, font=ft)
    
    for w in result_words:
        lt.insert("end", w)
    lt.pack(fill=tkinter.BOTH, expand=1)
    tk.mainloop()

def basic():
    global file_path, result_words
    if (not file_path) or len(file_path) == 0 :
        raise Exception("[error]请先选择要识别的图片")

    f = open(file_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    url = API_OCR_GENERAL_BASIC % (getAccessToken())
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=params, headers=headers)
    if response:
        data = response.json()
        result_words = map(lambda item: item["words"], data["words_result"])
    else:
        raise Exception("[error]请求数据失败，请检查网络")

def chooseImage():
    global file_path, tk
    if tk == None:
        init()

    current_path = os.getcwd()
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=[('PNG', '*.png *.jpg *.jpeg *.bmp *.webp')],
        initialdir=current_path
    )