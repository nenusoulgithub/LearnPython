import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://www.aqistudy.cn/historydata/index.php"

    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }

    # 请求页面信息
    page_text = requests.get(url=url, headers=headers).text

    # 解析页面数据
    r = etree.HTML(page_text)

    hot_lis = r.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li')

    hot_citys = []

    for li in hot_lis:
        hot_citys.append(li.xpath('./a/text()')[0])

    print(hot_citys)

    all_lis = r.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')

    all_citys = []

    for li in all_lis:
        all_citys.append(li.xpath('./a/text()')[0])

    print(all_citys)

    # 合并两组xpath表达式
    union_lis = r.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li | //div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')

    union_citys = []

    for li in union_lis:
        union_citys.append(li.xpath('./a/text()')[0])

    print(union_citys)