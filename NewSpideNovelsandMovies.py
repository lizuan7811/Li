#<video src="不能播的視頻".mp4"></video>
# 一般的視頻網站作法:
# 用戶上傳->轉碼(把式頻作處理，2K,1000,標清)->切片處理(把單個文件進行切片)
# 用戶在進行拉動進度條的時候有作用
# 需要一個文件紀錄:1.視頻撥放順序，2.視頻存放路徑
# M3U8 txt json =>文本
# 想要抓取一個視頻:
# 1.找到m3u8(各種手段)
# 2.通過m3u8下載到ts文件
# 3.可以過各種手段(不僅是編成手段)，把ts文件合併為一個mp4文件
import requests
import re
import asyncio
import aiohttp
import aiofiles
import os
# from Crypto.Cipher import AES 解密用的套件
# from bs4 import BeautifulSoup
# import xpath_parser
# from lxml import html
# from lxml import etree
# from lxml.etree import tostring
# import html
# url="https://dramasq.xyz/th210624/3.html"
# resp=requests.get(url)
# print(resp.text)
# resp.encoding="utf-8"
# htmlcont=resp.content.decode("utf-8")
# html=etree.HTML(htmlcont)
# print(html)
# FirVideoSrc=html.xpath('/html//div[2]/div[2]/div[6]/div/div[2]/div[1]/div[@id="video-player"]/iframe/text()')
# print(FirVideoSrc)

head={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
obj=re.compile(r"var m3u8url = '(?P<m3u8file>.*?)'.*?",re.S)

def get_iframe_src(url):
    resp=requests.get(url,headers=head)
    resp.encoding="utf-8"
    htmlcont=obj.search(resp.text).group("m3u8file")
    return htmlcont

def downloadM3U8File(url,name):
    resp=requests.get(url)
    with open(name,mode="wb")as f:
        f.write(resp.content)

async def download_ts(url,name,session1):
    async with session1.get(url) as resp:
        async with aiofiles.open(f"MOVIETRY/{name}",mode="wb")as f:
            # print(type(resp))
            # await print(f"{name}開始下載")
            await print(type(resp.content))
            await f.write(await resp.content.read())

    print(f"{name}下載完畢")

async def aio_downLoad(filename):
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(filename,mode="r",encoding="utf-8")as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line=line.strip()
                namem=line.split("/")[5]
                print(line)
                task=asyncio.create_task(download_ts(line,namem,session)) #這裡是創建任務#####這裡有疑惑######
                tasks.append(task)
            await asyncio.wait(tasks)
def mergeMovie(FileName):
#       apple拼接方式:cat 1.ts 2.ts 3.ts>xxx.mp4
#       window拼接方式copy /b 1.ts+2.ts+3.ts xxx.mp4
    lst=[]
    with open(FileName,mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line=line.strip()
            lst.append(f"MOVIETRY/{name}")
    s="+".join(lst)
    os.system(f"copy /b{s} movie.mp4")
    os.system(f"cat {s}>movie.mp4")
    print("Finished!")



def main(url):
    Movie_src=get_iframe_src(url)
    # Movie_src_resp=get_iframe_src(Movie_src)
    print(Movie_src)
    fileName="FirstMovie_1.txt"
    downloadM3U8File(Movie_src,fileName)
#下載視頻
#異步操作
    # SeconInnerNanme=
    asyncio.run(aio_downLoad("FirstMovie_1.txt"))
    mergeMovie(fileName)



if __name__=="__main__":
    url="https://dramasq.xyz/a/m3u8/?ref=_DqdQaHR0cHM6Ly92b2QuYnVuZWRpeS5jb20vMjAyMTA3MDgvMDl2dkx0SjcvaW5kZXgubTN1OA"
    main(url)







# url="https://www.91kanju.com/vod-play/12335-1-2.html"
# obj=re.compile(r".*?video:.*?url: '(?P<url>.*?)',",re.S) #用來提取M3U8檔案資源的地址
#
# resp=requests.get(url)
#
# # print(resp.text)
#
# m3u8_url=obj.search(resp.text).group("url")  #拿到m3u8的地址
#
# print(m3u8_url)
#
# resp2=requests.get(m3u8_url)
#
# with open("寒顫.m3u8",mode="wb") as f:
#     f.write(resp2.content)
#
# resp2.close()
# # print("下載完畢")
# ########下載M3U8的文件中資源影片檔案
# n=1
# with open("寒顫.m3u8",mode="r",encoding="utf-8") as f:
#     for line in f:
#         line=line.strip()  #先去掉空格、空白、換行符
#         if line.startswith("#"):
#             continue
#         print(line)
#
#         resp3=requests.get(line)
#         f=open(f"{n}.ts",mode="wb")
#         f.write(resp3.content)
#         n+=1


# import requests
# import html
# url="https://dushu.baidu.com/api/getCateDetail?channel=%E7%94%B7%E9%A2%91&cate2=%E4%B8%9C%E6%96%B9%E7%8E%84%E5%B9%BB&query=%E4%B8%9C%E6%96%B9%E7%8E%84%E5%B9%BB&count=10"
# resp=requests.get(url)
# resp.encoding="utf-8"
# print(html.escape(resp.content.decode("utf-8")))
