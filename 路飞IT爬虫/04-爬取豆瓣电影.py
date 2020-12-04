import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/new_search_subjects"
    # 录入头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    # 封装参数
    params = {
        "sort": "U",
        "range": "0,10",
        "tags": "",
        "start": "40",
        "genres": "喜剧",
    }
    # 发送request请求
    response = requests.get(url=url, params=params, headers=headers)
    # 接受返回的数据
    film_json = response.json()
    # 持久化
    with open("./爬取结果/豆瓣电影_{}.txt".format("喜剧"), "w", encoding="UTF-8") as fp:
        json.dump(film_json, fp, ensure_ascii=False)
    # 爬取完毕
    print("爬取完毕")