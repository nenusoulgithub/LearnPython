import requests

# 模拟浏览器UA伪装
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
if __name__ == '__main__':
    url = "https://www.so.com/s?ie=utf-8&fr=so.com&src=home_so.com"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 录入请求参数
    query = input("请输入查询词: ")
    param = {
        "q": query
    }
    # 加入请求参数
    response = requests.get(url=url, params=param, headers=headers)
    # 获取响应数据
    page = response.text
    # 持久化
    with open("./爬取结果/so_{}.html".format(query), "w", encoding="UTF-8") as fp:
        fp.write(page)
    # 爬取完毕
    print("爬取完毕")
