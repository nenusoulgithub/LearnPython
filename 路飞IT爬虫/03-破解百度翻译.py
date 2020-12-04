import requests

# 破解百度翻译
if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 封装参数
    kw = input("请输入翻译的词: ")
    data = {
        "kw": kw
    }
    # 使用POST请求
    response = requests.post(url=url, data=data, headers=headers)
    # 解析返回的JSON数据
    dict_json = response.json()
    # 持久化
    import json
    with open("./爬取结果/dict_{}".format(kw), "w", encoding="UTF-8") as fp:
        json.dump(dict_json, fp, ensure_ascii=False)
    # 爬取完毕
    print("爬取完毕")
