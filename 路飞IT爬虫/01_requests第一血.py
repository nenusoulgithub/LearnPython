import requests

if __name__ == '__main__':
    url = "https://www.sogou.com"
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    # test方法返回的就是页面的源码数据
    print(response.text)
    # 持久化存储
    with open("爬取结果/sogou.html", "w", encoding="UTF-8") as fp:
        fp.write(response.text)
    # 结束
    print("爬取完毕")
