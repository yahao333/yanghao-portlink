import gradio as gr
from yanghao.portlink import PortLinkClient as Client
import asyncio


# Global port configuration
PORT = 7860


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")


async def launchGradio():
    demo.launch(server_name="0.0.0.0", server_port=PORT)


async def main():
    gr_task = asyncio.create_task(launchGradio())
    # Expose port to the public internet. Check the debug output for the specific public URL.
    async with Client(PORT) as c:
        await c.link(PORT)


if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    await main()