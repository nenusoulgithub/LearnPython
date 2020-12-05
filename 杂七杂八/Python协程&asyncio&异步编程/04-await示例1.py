import asyncio


async def func():
    print("执行协程内部代码")
    response = await asyncio.sleep(2)
    print("执行结束", response)


if __name__ == '__main__':
    asyncio.run(func())
