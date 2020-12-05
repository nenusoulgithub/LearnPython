# 如何实例化bs4
from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open("./html.txt", "r", encoding="UTF-8")
    soup = BeautifulSoup(fp, "lxml")
    print(soup.div)
    # find的第一种用法
    print(soup.find("div"))
    # find的第二种用法属性定位
    print(soup.find("div", id="space-app"))
    # findall
    print(soup.find_all("meta"))
    # select选择器
    print(soup.select("#space-app"))
    print(soup.select(".abc"))
    # > 表示一个层级
    print(soup.select(".body > ul > li"))
    print(soup.select(".body > ul > li")[0])
    print("---------------------------------------")
    # 空格表示多个层级
    print(soup.select(".body > ul a"))
    print(soup.select(".body > ul a")[0])
    print(soup.select(".body > ul a")[0]['href'])  # 提取标签属性
    print("---------------------------------------")
    # 获取标签下的文本内容
    print(soup.select(".body")[0])
    print(soup.select(".body")[0].string)      # 获取标签的直系文本
    print(soup.select(".body")[0].get_text())  # 获取标签的所有文本
    print(soup.select(".body")[0].text)        # 获取标签的所有文本
