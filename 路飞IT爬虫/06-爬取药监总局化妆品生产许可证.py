import requests
import json

if __name__ == '__main__':
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    page = 1
    page_count = 1
    while True:
        print("爬取第{}页数据".format(page))
        # 封装参数
        data = {
            "on": "true",
            "page": page,
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
        }
        # 发送POST请求
        response = requests.post(url=url, data=data, headers=headers)
        # 解析返回的JSON
        try:
            # 解析返回的JSON
            """
            'pageCount': 360, 'pageNumber': 1, 'pageSize': 15, 'property': '', 'totalCount': 5390
            """
            page_json = response.json()
            page_count = page_json["pageCount"]
            page_number = page_json["pageNumber"]
            # 爬取许可证信息
            xkz_list = page_json["list"]
            with open("./爬取结果/药监总局化妆品生产许可证信息.txt", "a", encoding="UTF-8") as fp:
                for xkz in xkz_list:
                    print(xkz["ID"], xkz["EPS_NAME"])

                    xkz_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
                    # 封装参数
                    data = {
                        "id": xkz["ID"],
                    }
                    # 发送POST请求
                    response = requests.post(url=xkz_url, data=data, headers=headers)
                    # 解析返回的JSON
                    page_json = response.json()
                    # 持久化数据
                    json.dump(page_json, fp, ensure_ascii=False)
                    fp.write("\n")
        except Exception:
            print("解析失败")

        page += 1

        if page > page_count:
            break