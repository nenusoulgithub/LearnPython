import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://bj.58.com/ershoufang/"

    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }

    # 请求页面信息
    page_text = requests.get(url=url, headers=headers).text

    with open("./58.html", "w", encoding="UTF-8") as fo:
        fo.write(page_text)

    # 解析页面数据
    r = etree.HTML(page_text)

    li_list = r.xpath('//ul[@class="house-list-wrap"]/li[@class="sendsoj"]')

    for li in li_list:
        print(li.xpath('./div[@class="list-info"]/h2/a/text()')[0])

