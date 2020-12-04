# 对首页的页面数据进行爬取

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 《三国演义》
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    # 请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 请求首页内容
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    # 解析章节标题
    menu_list = soup.select(".book-mulu > ul > li")
    for menu_tag in menu_list:
        menu_soup = BeautifulSoup(str(menu_tag), "lxml")
        menu_title = menu_soup.find("a").text
        menu_url = "https://www.shicimingju.com{}".format(menu_soup.find("a")['href'])
        print("开始爬取【{},{}】".format(menu_title, menu_url))
        chapter_page = requests.get(url=menu_url, headers=headers)
        chapter_soup = BeautifulSoup(chapter_page.text, "lxml")
        chapters = chapter_soup.select(".chapter_content p")
        with open("./爬取结果/三国演义/{}.txt".format(menu_title), "w", encoding="UTF-8") as fp:
            for chapter in chapters:
                fp.write(chapter.text + "\n")
