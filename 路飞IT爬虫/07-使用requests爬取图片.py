import requests

if __name__ == '__main__':
    url = "https://pic.qiushibaike.com/system/pictures/12378/123785183/medium/QGZ0QNTBC3DLFIH4.jpg"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 请求图片
    img = requests.get(url=url, headers=headers).content
    # 持久化图片
    with open("爬取结果/糗事百科/糗图1.jpg", "wb") as fp:
        fp.write(img)
