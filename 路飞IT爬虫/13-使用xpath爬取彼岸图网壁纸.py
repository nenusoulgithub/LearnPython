import requests
from lxml import etree

if __name__ == '__main__':
    url = "http://pic.netbian.com/4kdongman/"

    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }

    # 请求页面信息
    page_text = requests.get(url=url, headers=headers).text

    # 解析页面数据
    r = etree.HTML(page_text)

    li_list = r.xpath('//div[@class="slist"]/ul/li')

    for li in li_list:
        img_src = "http://pic.netbian.com/" + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]
        img_name = img_name.encode("iso-8859-1").decode("GBK")
        img_data = requests.get(img_src, headers=headers).content
        with open("./爬取结果/彼岸图网/{}.jpg".format(img_name), "wb") as fo:
            fo.write(img_data)
            print(img_name + "下载成功！")


