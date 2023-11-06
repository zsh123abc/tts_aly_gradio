"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/10/12 15:18
@Filename			: voide_ali.py
@Description		: 
@Software           : PyCharm
"""
import io
import time
import threading
import sys

import nls
import requests
import time


URL = "wss://nls-gateway-cn-shenzhen.aliyuncs.com/ws/v1"

url = 'https://ai.umi6.com:28083/api/sv_voice/ali_token'
response = requests.get(url=url)

if response.status_code == 200:
    data = response.json()
    token = data['data']['token']

TOKEN = token  # 参考https://help.aliyun.com/document_detail/450255.html获取token
APPKEY = "ccR3tWBwNilIBRKL"  # 获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist


# TEXT = "今天天气很好"

# 以下代码会根据上述TEXT文本反复进行语音合成
class DemoTts:
    def __init__(self, tid):
        # self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid

    def start(self, text,output_wav,voice):
        self.__text = text
        # self.__f = io.BytesIO()
        self.__f = open(output_wav, "wb")
        self.__test_run(voice)

    def test_on_metainfo(self, message, *args):
        print("on_metainfo message=>{}".format(message))

    def test_on_error(self, message, *args):
        print("on_error args=>{}".format(args))

    def test_on_close(self, *args):
        print("on_close: args=>{}".format(args))
        print(self.__f)
        try:
            self.__f.close()
        except Exception as e:
            print("close file failed since:", e)

    def test_on_data(self, data, *args):
        try:
            print(data)
            self.__f.write(data)
        except Exception as e:
            print("write data failed:", e)

    def test_on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))
        message.json()
        print(message)
    def __test_run(self,voice):
        print("thread:{} start..".format(self.__id))
        tts = nls.NlsSpeechSynthesizer(url=URL,
                                       token=TOKEN,
                                       appkey=APPKEY,
                                       on_metainfo=self.test_on_metainfo,
                                       long_tts=True,
                                       on_data=self.test_on_data,
                                       on_completed=self.test_on_completed,
                                       on_error=self.test_on_error,
                                       on_close=self.test_on_close,
                                       callback_args=[self.__id])
        print("{}: session start".format(self.__id))
        ex = {"enable_ptts": True}
        r = tts.start(self.__text, voice="zhixiaobai", aformat="wav", ex=ex)
        print("{}: tts 完成:{}\n".format(self.__id, r))
        # return self.__f




def tts_input_text(text,voice,output_wav):
    TEXT = text
    output_wav += "/out.wav"
    nls.enableTrace(True)
    t = DemoTts("name")
    t.start(TEXT,output_wav,voice)


def tts_upload_file(file_path, voice, output_wav):
    with open(file_path, "r", encoding="utf-8") as file:
        # 读取文件内容
        text = file.read()
    output_wav += "/out.wav"
    TEXT = text
    nls.enableTrace(True)
    t = DemoTts("name")
    t.start(TEXT,output_wav,voice)



def run(num, file_path, voice, output_wav):
    num = input("!!!  输入1或2\n1-输入文本\n2-上传文件") 
    if num == '1':
        text = input() 
    elif num == '2':
        file_path = input("请输入文件完整路径") 
        with open(file_path, "r", encoding="utf-8") as file:
            # 读取文件内容
            text = file.read()

    voice = input("输入声音voice")
    
    TEXT = text
    output_wav = input("填写输入文件的保存路径")

    nls.enableTrace(True)
    t = DemoTts("name")
    t.start(TEXT,output_wav,voice)


# while True:
#     print("-"*25)
#     text = ''
#     print("!!!  选择-1-或-2-  !!!\n输入文本---1\n上传文件---2\n退出程序---3")
#     print("-"*25)
#     num = input("请输入(1或2或3)：") 
    

#     if num.isdigit():
#         if num == '1':
#             print("\n"+"-"*5+'文本'+'-'*5)
#             text = input("输入 文本 合成语音(输入你想合成的文本)：") 
#         elif num == '2':
#             print("\n"+"-"*5+'文件'+'-'*5)
#             file_path = input("请输入 文本(.txt) 文件完整路径：") 
#             with open(file_path, "r", encoding="utf-8") as file:
#                 # 读取文件内容
#                 text = file.read()
#         elif num == '3':
#             count = 5
#             while True:
#                 print(f"{count}秒之后自动退出", end="\r")  # 使用"\r"覆盖前一个数字的输出
#                 count -= 1
#                 time.sleep(1)
#                 if count==0:
#                     break
#     else:
#         print("\n！！！无效输入，输入数字1,2,3\n")
#         continue
#     voice = input("输入声音voice：")

#     TEXT = text
#     output_wav = input("填写输入文件的保存路径：")
#     output_wav += "/out.wav"
#     print("\n开始语音合成...")
#     print("稍等...")

#     nls.enableTrace(True)
#     t = DemoTts("name")
#     t.start(TEXT,output_wav,voice)


    # print("")
    # count = 5
    # while True:
    #     print(f"{count}秒之后自动退出", end="\r")  # 使用"\r"覆盖前一个数字的输出
    #     count -= 1
    #     time.sleep(1)
    #     if count==0:
    #         break
