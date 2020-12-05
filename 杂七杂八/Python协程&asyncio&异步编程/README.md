# 协程 & asyncio & 异步编程

## 如何讲解

- 第一部分：协程
- 第二部分：asyncio模块异步编程
- 第三部分：实战案例

## 1. 协程
协程不是计算机提供，程序员认为制造。

协程(Coroutine)，也可以称为微线程。是一种用户态的上下文切换技术，也就是通过一个线程实现代码块的相互切换执行。例如：

```python
def func1():
    print(1)
    ...
    print(2)

def func2():
    print(3)
    ...
    print(4)

func1()
func2()
```

实现协程的几种方法：
- greenlet，早期模块。
- yield关键字。
- asyncio装饰器（py3.4）。
- async、await关键字（py3.5）【最主流，python官方推荐】。

### 1.1 通过greenlet实现协程

```
pip3 install greentlet
```

```python
from greenlet import greenlet

def func1():
    print(1)
    gr2.switch() # 第二步：切换到func2执行
    print(2)
    gr2.switch() # 第四步：切换到func2执行

def func2():
    print(3)
    gr1.switch() # 第三步：切换到func1执行
    print(4)
    gr1.switch() # 第五步：切换到func1执行

gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch() # 第一步：去执行func1函数
```

### 1.2 yield关键字

```python
def func1():
    yield 1
    yield from func2() # 跳到func2执行
    yield 2

def func2():
    yield 3
    yield 4

f1 = func1()
for item in f1:
    print(item)
```

### 1.3 asyncio

一定是python3.4之后的版本

```python
import asyncio

@asyncio.coroutine
def func1():
    print(1)
    # 比如当前IO是网络IO，比如下载图片
    yield from asyncio.sleep(2)  # 遇到io耗时操作，自动切换到task中其他任务
    print(2)

@asyncio.coroutine
def func2():
    print(3)
    # 磁盘IO加载一个文件
    yield from asyncio.sleep(2) # 遇到io耗时操作，自动切换到task中其他任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_in_executor(asyncio.wait(tasks))
```

**注意：** 遇到IO操作自动切换.

### 1.3 async & await

在python3.5以后使用

```python
import asyncio

async def func1():
    print(1)
    # 比如当前IO是网络IO，比如下载图片
    await asyncio.sleep(2)  # 遇到io耗时操作，自动切换到task中其他任务
    print(2)

async def func2():
    print(3)
    # 磁盘IO加载一个文件
    await asyncio.sleep(2) # 遇到io耗时操作，自动切换到task中其他任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_in_executor(asyncio.wait(tasks))
```

通常情况下使用 1.1 和 1.4

## 2. 协程的意义
在一个线程中，如果遇到IO等待的时间，不会让线程傻傻地等待，利用空闲事件完成其他任务。
案例：去下载三张图片（网络IO）。

## 3. 基于协程的异步编程

### 3.1 事件循环
理解成一个死循环，去检测并执行某些代码。
```伪代码
任务列表 = [任务1, 任务2, 任务3,...]

while True:
    可执行任务列表, 已完成任务列表 = 去任务裂变中遍历
    
    for 就绪任务 in 可执行任务列表：
        执行就绪任务

    for 已完成任务 in 已完成任务列表:
        在任务列表中删除

    如果任务列表中的任务都完成 ，种植循环
```

```python
import asyncio

# 去生成并获取一个事件循环
loop = asyncio.get_event_loop()
# 将任务当道任务列表
loop.run_until_complete(任务)
```

### 3.2 快速上手
协程函数：async def 函数名。
协程对象，执行协程函数()得到的对象。

```python
async def func():
    pass

result = func()
```
**注意：**执行协程函数创建协程对象，函数内部代码不会执行。

如果想要运行协程函数内部代码，必须要将协程对象校对事件循环来处理。

```python
import asyncio

async def func():
    print("协程函数")

result = func()
# 第一种方式
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
# 第二种方式
asyncio.run(result)
```

### 3.3 await

await后面可以跟（协程对象，feature，tasks）

示例1:
```python
import asyncio


async def func():
    print("来玩啊...")
    response = await asyncio.sleep(2)
    print("结束", response)


if __name__ == '__main__':
    asyncio.run(func())
```

示例2：
```python
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
```

示例3：
```python
import asyncio


async def sub_func():
    response = await asyncio.sleep(2)
    return "我回来了!"


async def func():
    print("执行协程内部代码")
    response = await sub_func()
    print("执行结束", response)
    response = await sub_func()
    print("执行结束", response)

if __name__ == '__main__':
    asyncio.run(func())
```

### 3.4 task对象

帮助你在事件循环中添加多个任务，通过asyncio.create_task()来创建。

示例1：
```python
import asyncio


async def func():
    print("开始执行协程内部工作")
    response = await asyncio.sleep(2)
    print("执行完毕", response)
    return "执行结果"


async def main():
    print("main开始")

    # 创建task对象，将当前执行函数任务添加到事件循环内部
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换到其他任务。
    # 此处的await是等待对象的协程全部执行结束，并打印结果。
    ret1 = await task1
    ret2 = await task2

    print(ret1, ret2)

if __name__ == '__main__':
    asyncio.run(main())
```

示例2：
```python
import asyncio


async def func():
    print("开始执行协程内部工作")
    response = await asyncio.sleep(2)
    print("执行完毕", response)
    return "执行结果"


async def main():
    print("main开始")

    # 创建task对象，将当前执行函数任务添加到事件循环内部
    task_list = [
        asyncio.create_task(func(), name="协程任务-1"),
        asyncio.create_task(func(), name="协程任务-2"),
    ]

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换到其他任务。
    # 此处的await是等待对象的协程全部执行结束，并打印结果。
    done, pending = ret1 = await asyncio.wait(task_list)

    print(done)

if __name__ == '__main__':
    asyncio.run(main())
```

示例3：
```python
import asyncio


async def func():
    print("开始执行协程内部工作")
    response = await asyncio.sleep(2)
    print("执行完毕", response)
    return "执行结果"


if __name__ == '__main__':
    print("main开始")

    # 创建task对象，将当前执行函数任务添加到事件循环内部
    task_list = [
        func(),
        func(),
    ]

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动切换到其他任务。
    # 此处的await是等待对象的协程全部执行结束，并打印结果。
    done, pending = ret1 = asyncio.run(asyncio.wait(task_list))

    print(done)
```

### 3.5 asyncio.Future对象

Future对象是一个底层的对象，是Task的基类。

示例1：
```python
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

```

示例2：
```python
import asyncio


async def func(fut):
    await asyncio.sleep(2)
    fut.set_result(666)


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个Future对象，这个对象什么都不干
    fut = loop.create_future()

    # 创建一个任务
    loop.create_task(func(fut))

    # 等待任务最终结果（future对象），没有结果会一直等下去。
    await fut


if __name__ == '__main__':
    asyncio.run(main())

```

### 3.6 concurrent_futures_future

使用线程池，进程池实现异步时用到的对象。

### 3.7 async + 不支持async的模块混合使用

示例代码

```python
import asyncio
import requests


async def download_image(url):
    print("下载图片%s" % url)
    # 发送强求下载图片
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
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

    task_list = [download_image(url) for url in urls]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))

```

### 3.6 异步可迭代对象

示例：
```python
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
```

### 3.8 异步上下文管理器

通过实现__aenter__()和__aexit()__来实现对异步上下文环境的控制

```python
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
```

# 4. uvloop

是asyncio的事件循环的替代方案，效率高于原生的。

