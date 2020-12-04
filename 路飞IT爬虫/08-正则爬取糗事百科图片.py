import requests
import re

"""
<div class="thumb">
<img src="//pic.qiushibaike.com/article/image/LS8SUJFI0LFO7HTR.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/IT0ZUYHR2TD88UJP.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/3PP3LB9VE05VRWRH.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/ZOR33X7DBZQ9HMYL.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/ZZ38TR91CI2IR5EK.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/D38E4K6UYQSJ8VL2.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/SIYVPLNWXZJWSNDT.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/YXK7Q04RO77GS21B.jpg" alt="猫咪戴上各种款式的帽">
</div>
正则: <div class="thumb">.*?<img src="(.*?)" alt.*?</div>
正则: <div class="thumb">(<img.*?>)</div>
"""

if __name__ == '__main__':
    page_context = """
<div class="thumb">
<img src="//pic.qiushibaike.com/article/image/LS8SUJFI0LFO7HTR.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/IT0ZUYHR2TD88UJP.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/3PP3LB9VE05VRWRH.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/ZOR33X7DBZQ9HMYL.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/ZZ38TR91CI2IR5EK.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/D38E4K6UYQSJ8VL2.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/SIYVPLNWXZJWSNDT.jpg" alt="猫咪戴上各种款式的帽">
<img src="//pic.qiushibaike.com/article/image/YXK7Q04RO77GS21B.jpg" alt="猫咪戴上各种款式的帽">
</div>
    """

    thumb_div = re.findall('<div class="thumb">\n(.*?)\n</div>', page_context, re.S)

    if thumb_div.__len__() == 1:
        img_divs = re.findall("<img.*?>", thumb_div[0], re.S)
        for img_div in img_divs:
            img_src = re.findall('<img src="//(.*?)" alt=".*?">', img_div)
            if img_src.__len__() == 1:
                print(img_src[0])
                img_name = re.findall('image/(.*?.jpg)', img_src[0])
                # 录入头信息
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
                }
                # 请求图片
                img = requests.get(url="http://{}".format(img_src[0]), headers=headers).content
                with open("./爬取结果/糗事百科/{}".format(img_name[0]), "wb") as fp:
                    fp.write(img)





