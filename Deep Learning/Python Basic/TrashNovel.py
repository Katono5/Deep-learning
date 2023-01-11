import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os,time,random

url="https://www.meitulu.com/item/16559.html"

class dl_plmm:
    def __init__(self,url):
        self.url=url
        urlinfo=urlparse(url)

        #self.baseurl用来存储域名，即：https://www.meitulu.com
        self.baseurl=urlinfo.scheme+"://"+urlinfo.netloc
        print(self.baseurl)

        #生成一个集合用来去重，该集合用于存储分页链接
        self.page_links=set()

    #打开页面并获取内容
    def openurl(self,url):
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
            "Referer":"https://www.meitulu.com/t/aiyouwu/"
        }
        
        #请求页面，并且请求头包含了浏览器信息和Referer，如果没有Referer，是无法请求到图片的
        res=requests.get(url,headers=headers)
        if res.status_code == 200:
            #返回页面的内容
            return res.content
        else:
            print(res.text)


    #获取所有列表页链接
    def store_page_links(self):
        content=self.openurl(self.url)
        soup=BeautifulSoup(content,"html.parser")
        page_tags=soup.find("div",attrs={"id":"pages"}).find_all("a")
        for page_tag in page_tags:
            self.page_links.add(page_tag['href'])

    #访问所有列表页并下载图片
    def dl_imgs(self,page_link):
        page_content=self.openurl(self.baseurl+page_link)  #列表页的链接是不含域名的，这里将它拼接为完整url
        soup=BeautifulSoup(page_content,"html.parser")
        img_tags=soup.find("div",class_="content").find("center").find_all("img")

        if len(self.page_links)==0:
            return

        for img_tag in img_tags:
            img_src=img_tag["src"]
            print("下载图片:%s" % (img_src))
            img_content=self.openurl(img_src)
            #print(img_content)

            #定义文件名，文件名用时间戳和随机数字命名，以避免文件名有重复
            fn=str(int(time.time()))+str(random.randint(100,999))+".jpg"
            with open(fn,"wb") as f:
                f.write(img_content)

    #开始运行
    def run(self):
        #获取所有page的url
        self.store_page_links()
        
        #如果不存在imgs文件夹，就创建一个imgs文件夹
        if not os.path.isdir("imgs"):
            os.mkdir("imgs")

        #切换当前目录为imgs
        os.chdir("imgs")

        #下载图片
        for page_link in self.page_links:
            self.dl_imgs(page_link)


spider=dl_plmm(url)
spider.run()
