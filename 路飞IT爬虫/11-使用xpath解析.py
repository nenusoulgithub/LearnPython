from lxml import etree

# 获取一个etree对象
# 1. 从本地文件获取 etree.parse()
# 2. 从互联网爬取的网页原码 etree.HTML()
if __name__ == '__main__':
    r = etree.parse("./58.html")

    li_list = r.xpath('//ul[@class="house-list-wrap"]/li')

    for li in li_list:
        print(li.xpath('//div[@class="list-info"]/h2/a/text()'))

    # tree.xpath("/html/head/title")
    # tree.xpath("/html/body/div")
    # # 这个//返回多个层级的对象
    # tree.xpath("/html//div")
    # # 这个//从任意位置定位div标签
    # tree.xpath("//div")
    # # 属性定位，获取标签内部的文本内容
    # # /text(): 获取直系文本内容
    # print(tree.xpath('//div[@class="body"]/ul/li[2]/a/text()')[0])
    # # //text(): 获取所有的文本内容
    # print(tree.xpath('//div[@class="body"]/ul/li[4]//text()'))
    # # /@attr_name: 获取属性值
    # print(tree.xpath('//div[@class="body"]/@id'))


