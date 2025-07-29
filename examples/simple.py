from yanghao.portlink import PortLinkClient as Client

async def main():
    # 这里是把8000端口映射到公网, 具体公网地址查看输出的调试信息
    async with Client(8000) as c:
        await c.link(8000)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
