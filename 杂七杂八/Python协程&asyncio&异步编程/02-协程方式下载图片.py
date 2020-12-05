import asyncio
import aiohttp


async def fetch_image(session, url):
    print("发送请求%s" % url)
    # 发送强求下载图片
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        # 图片保存到本地文件
        file_name = url.rsplit('_')[-1]
        with open(file_name, "wb") as file_object:
            file_object.write(content)


async def download_image():
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604490371101&di=b741ca405e4086a3f6373d497184d025&imgtype=0&src=http%3A%2F%2Fp6.qhimg.com%2Ft01c08a75007a4c9e80.jpg",
            "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604489496625&di=e8f11a27c0f77d5f8f711179b3a8490f&imgtype=0&src=http%3A%2F%2Fimage.bubuko.com%2Finfo%2F201912%2F20191209101647542957.jpg",
            "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1604489510424&di=15a6b56f0b80894ebce29af7129b1e63&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171221%2Ff6e8db0e4690438baaaa2395f8bc8a92.jpeg"
        ]

        tasks = [asyncio.create_task(fetch_image(session, url)) for url in urls]

        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(download_image())
