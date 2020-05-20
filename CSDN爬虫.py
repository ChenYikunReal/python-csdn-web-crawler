import random
import requests
import re
import time

'''
这是一个简单的单线程爬虫，没有什么特别复杂的内容，使用体验还算可以。
没有安装相关的库是不能运行的呦。

另外，必须要写在前面的话：
博客平台为我们学习和查阅资料提供了很大的便利，希望大家不要用高速的爬虫破坏它。
本爬虫代码仅供学习参考，请大家不要使用它去疯狂刷新访问量，感谢。
'''

payload = ""

# 请求头信息（提交前已删除Cookie，可以自己加上，格式同下）
headers = {
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
}


# 定义函数，用于获得文章的URL列表
def get_urls(your_url):
    # 发送请求
    response = requests.request("GET", your_url, data=payload, headers=headers)
    # 设置解码方式
    response.encoding = response.apparent_encoding
    # 解码
    html_source = response.text
    # 基于正则表达式获取网页中的URL
    all_urls = re.findall("https://[^>\";\']*\\d", html_source)
    useful_urls = []
    for u in all_urls:
        if ('details' in u) and (u not in useful_urls):
            useful_urls.append(u)
    return useful_urls


# 把your_url换成你的主页URL：https://blog.csdn.net/XXXX，获得文章的URL列表
urls = get_urls("your_url")

# 死循环运行爬虫，只有手动停掉或是连接中断才能停下来
while True:
    for url in urls:
        # 使用GET刷访问量
        requests.request("GET", url, data=payload, headers=headers)
        # 打印访问信息，确认访问情况
        print(url, " 访问完成")
        # 别刷太快 & 用随机数的方式尽可能避免被封IP
        time.sleep(random.randint(5, 15))
    time.sleep(random.randint(20, 30))
