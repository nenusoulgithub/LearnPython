import asyncio


async def func():
    print("协程函数")

result = func()
# 第一种方式
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)
# 第二种方式
asyncio.run(result)
