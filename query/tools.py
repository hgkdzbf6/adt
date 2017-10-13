# -*- coding:utf-8 -*- 
# 
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re
import json
import base64
import requests
import os
# 导入百度的图像识别库吧

class Tool:

    def __init__(self):
        self.url = ''
    
    def get_text(self,url):
        data=self.get_page(url)
        return self.url_parse(data)

    def get_page(self,url):

        self.url = url
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        try:
            res=response.read().decode('utf-8','ignore')
        except e:
            try:
                res=response.read().decode('gbk', 'ignore')
            except e:
                pass
            pass

        return res

    def find_label(self,label):
        new_text=''
        list=self.soup.find_all('p')
        for item in list:
            new_text+=item.get_text()
        return new_text

    def url_parse(self,data):
        text=''
        self.soup = BeautifulSoup(data)
        text+=self.find_label('p')
        text+=self.find_label('pre')
        return text


class PicTool:
    # pic -> base64 encode picture data
    def __init__(self,image):
        self.app_id='10217591'
        self.api_key='ARsY22uGsXL3U6EAGugmmcDW'
        self.secret_key='kMfrNalr9ylD9YUbMp6Bkf5a4gCRG5mD'
        image_str=image
        #还要做掐头去尾的工作= =
        position=image_str.find('base64,')
        if position>0:
            image_str=image_str[position+7:]
        else:
            position=image_str.find('"b\'')
            if position>0:
                image_str=image_str[position+3:]

        self.image=image_str
        # self.save_img()
        pass

    def save_img(self):
        # print(self.image.encode('utf-8'))
        print(len(self.image.encode('utf-8')))
        imgdata=base64.b64decode(self.image.encode('utf-8'))  
        file=open('1.png','wb')  
        file.write(imgdata)  
        file.close()  

    def get_json(self):
        header={}
        host = 'https://aip.baidubce.com/oauth/2.0/token?'+\
        'grant_type=client_credentials&'+\
        'client_id='+self.api_key+\
        '&client_secret='+self.secret_key
        # print(host)
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        content=str(content,'utf-8')
        data=json.loads(content)
        if (data):
            print(data['access_token'])
        access_token=data['access_token']
        content_type='application/x-www-form-urlencoded'
        self.url_data=access_token
        header['content_type']=content_type
        # data=urllib.parse.urlencode({'image':self.image})
        self.data={'image':self.image}
        self.headers=header
        #print(pic)
        #
        
    def post_data(self):        
        self.get_json()
        url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='+self.url_data
        # print(self.data)
        request=requests.post(url,data=self.data,headers=self.headers) 
        return request.text

    def get_text(self):
        data=self.post_data()
        receive=json.loads(data)
        str=''
        word_list=receive['words_result']
        for i in range(len(word_list)):
            str=str+word_list[i]['words']
        return str