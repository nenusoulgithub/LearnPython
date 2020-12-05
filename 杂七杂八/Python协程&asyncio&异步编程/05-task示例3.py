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
