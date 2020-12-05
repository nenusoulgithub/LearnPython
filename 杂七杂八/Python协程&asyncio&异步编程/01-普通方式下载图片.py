import requests


def download_image(url):
    print("下载图片%s" % url)
    # 发送强求下载图片
    response = requests.get(url)
    print("下载完成")
    # 图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name, "wb") as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    urls = [
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604489476805&di=91153030ab3d0581401d82d9d2406aac&imgtype=0&src=http%3A%2F%2Fshp.qpic.cn%2Fqqvideo_ori%2F0%2Fg0857o2eaih_496_280%2F0",
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604489496625&di=e8f11a27c0f77d5f8f711179b3a8490f&imgtype=0&src=http%3A%2F%2Fimage.bubuko.com%2Finfo%2F201912%2F20191209101647542957.jpg",
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604489510424&di=15a6b56f0b80894ebce29af7129b1e63&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171221%2Ff6e8db0e4690438baaaa2395f8bc8a92.jpeg"
    ]

    for url in urls:
        download_image(url)
