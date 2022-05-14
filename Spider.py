import requests
import os
from urllib import parse
import re
import time

class BingImageSpider():
    
    def __init__(self):
        self.url = 'https://cn.bing.com/images/async?q={}&first=66&count=35&cw=1519&ch=379&relp=30&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*1340_y*781_h*180_c*5_i*31_r*5'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def get_images(self,full_url,word):
        req = requests.get(url=full_url,headers=self.headers)
        req.encoding='utf-8'
        html = req.text
        
        # test
        #testfilename = word+'.html'
        #with open(testfilename,'wb') as g:
        #    g.write(html)
        
        pattern = re.compile('https://tse[0-9]-mm.cn.bing.net+?[A-Za-z0-9//?.&-=]+',re.S)
        pattern_html = pattern.findall(html)
        print(pattern_html)

        directory = './images/'

        if os.path.exists(directory) != True:
            os.mkdir(directory)
        
        i = 1
        for image_link in pattern_html:
            filename = directory+word+'_{}.jpg'.format(i)
            self.save_images(image_link,filename)
            i+=1
        
    
    def save_images(self,image_link,filename):
        time.sleep(1)
        image = requests.get(url = image_link,headers = self.headers).content
        
        with open(filename,'wb') as f:
            f.write(image)

        print(filename,'Download seccess!')
        


    def run(self):
        word = input('Please input search word:')
        params = parse.quote(word)
        full_url = self.url.format(params)
        self.get_images(full_url,word)


if __name__ == '__main__':
    spider = BingImageSpider()
    spider.run()
