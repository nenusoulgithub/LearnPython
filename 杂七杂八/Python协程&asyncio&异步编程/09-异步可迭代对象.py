import asyncio


class Reader(object):
    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count >= 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def func():
    reader = Reader()
    async for line in reader:
        print(line)


if __name__ == '__main__':
    asyncio.run(func())