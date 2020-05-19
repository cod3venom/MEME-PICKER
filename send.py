import requests
import os
import time
from static import *
from tqdm import tqdm
class Send_todb:
    def image_name(self,img):
        if img is not None:
            if '/' in img:
                count = img.count('/')
                img = img.split('/')[count]
        return img
    

    def cache(self,file):
        name = memedir+self.image_name(file)
        real_url = self.image_name(file)
        _bin = requests.get(file, stream = True)
        _sz = int(_bin.headers['content-length'])
        with open(name,"wb") as _w:
            for data in tqdm(range(int(936))):
                _w.write(_bin.content)
            print("[+] DOWNLOADED -> " + str(_sz) + " KB")
            self.send_data(real_url)
    def send_data(self,img):
        data = {"pymachine":"","pyimage":"/memes/"+img}
        sender = requests.post(my_db_url,data)
        print(sender.text)
        _progress=False
