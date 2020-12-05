import asyncio


async def sub_func():
    response = await asyncio.sleep(2)
    return "我回来了!"


async def func():
    print("执行协程内部代码")
    response = await sub_func()
    print("执行结束", response)

if __name__ == '__main__':
    asyncio.run(func())
