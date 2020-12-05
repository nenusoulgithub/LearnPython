import requests
import json
import math

if __name__ == '__main__':
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 封装post请求参数
    data = {
        "cname": "",
        "pid": "",
        "keyword": "北京",
        "pageIndex": "1",
        "pageSize": "10",
    }
    # 发送POST请求
    response = requests.post(url=url, data=data, headers=headers)
    # 接受返回参数
    page_text = response.text
    page_json = json.loads(page_text)
    print(page_json)
    # 解析返回文本
    row_count = page_json["Table"][0]["rowcount"]
    print("地址总行数：{}".format(row_count))
    page_count = math.ceil(row_count / 10)
    print("地址总页数：{}".format(page_count))
    with open("爬取结果/肯德基地址.txt", "w", encoding="UTF-8") as fp:
        for address in page_json["Table1"]:
            fp.write(str(address) + "\n")

    for page_index in range(2, page_count + 1):
        print("爬取第{}页的地址信息".format(page_index))
        # 封装post请求参数
        data = {
            "cname": "",
            "pid": "",
            "keyword": "北京",
            "pageIndex": page_index,
            "pageSize": "10",
        }
        # 发送POST请求
        response = requests.post(url=url, data=data, headers=headers)
        # 接受返回参数
        page_text = response.text
        page_json = json.loads(page_text)
        print(page_json)
        # 持久化数据
        with open("爬取结果/肯德基地址.txt", "a", encoding="UTF-8") as fp:
            for address in page_json["Table1"]:
                fp.write(str(address) + "\n")
    # 爬取结束
    print("爬取结束")