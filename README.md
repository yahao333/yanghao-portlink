# `yanghao.portlink`

[简体中文](README.cn.md)

> A Python library to expose your local port to the public internet.

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Local App     │    │  yanghao.portlink │    │   Public Web    │
│  (Port 8000)    │◄──►│     Tunnel       │◄──►│  (Public URL)   │
│                 │    │                  │    │                 │
│  127.0.0.1:8000 │    │  Secure Bridge   │    │ https://xxx.com │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        ▲                        ▲                        ▲
        │                        │                        │
   Your Local                 Library                 Internet
   Application               Magic ✨                 Access
```

```bash
pip install yanghao.portlink
```

---

## 🚀 Quick Start

1.  **Install**
    ```bash
    pip install yanghao.portlink
    ```

2.  **Programmatic usage**

    ```python
    from yanghao.portlink import PortLinkClient as Client

    async def main():
        # Expose port 8000 to the public internet. Check the debug output for the specific public URL.
        async with Client(8000) as c:
            await c.link(8000)

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
    ```

3.  **Google Colab Example**

    For Google Colab users, check out our [Colab example](examples/colab.py) that demonstrates how to expose Gradio applications to the public internet.

---

## ✨ Features

-   **Zero-config** – simple to use
-   **TCP protocol** – simple and reliable
-   **Auto-reconnect** – survives network hiccups
-   **Cross-platform** – Linux, macOS, Windows

---


## 🤝 Contributing

1.  Fork the repo
2.  `pip install -e ".[dev]"`
3.  `pytest` (≥ 90 % coverage required)
4.  Open a PR

---

## 📄 License

MIT © 2025 yahao333

---

## 💬 Help

-   `https://github.com/yahao333/portlink/discussions`
-   `https://github.com/yahao333/portlink/issues`