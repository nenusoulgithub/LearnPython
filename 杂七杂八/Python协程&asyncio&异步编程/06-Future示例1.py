import asyncio


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个Future对象，这个对象什么都不干
    fut = loop.create_future()

    # 等待任务最终结果（future对象），没有结果会一直等下去。
    await fut


if __name__ == '__main__':
    asyncio.run(main())
