from yanghao.portlink import PortLinkClient as Client

async def main():
    # Expose port 8000 to the public internet. Check the debug output for the specific public URL.
    async with Client(8000) as c:
        await c.link(8000)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
