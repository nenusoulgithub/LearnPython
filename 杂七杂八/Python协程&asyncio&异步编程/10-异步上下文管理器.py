import asyncio


class AsyncContextManager(object):
    def __init__(self, conn):
        self.conn = conn

    async def do_something(self):
        return 666

    async def __aenter__(self):
        print("执行__aenter__函数")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("执行__aexit__函数")
        await asyncio.sleep(2)


async def func():
    async with AsyncContextManager("异步上下文管理器") as manager:
        result = await manager.do_something()
        print(result)


if __name__ == '__main__':
    # 第一种调用方式
    # asyncio.run(func())
    # 第二种启动方式
    tasks = [func()]
    asyncio.run(asyncio.wait(tasks))