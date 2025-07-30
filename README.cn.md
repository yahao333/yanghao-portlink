# `yanghao.portlink`

> 一个用于将本地端口暴露到公网的 Python 库。

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   本地应用      │    │  yanghao.portlink │    │   公网访问      │
│  (端口 8000)    │◄──►│     隧道服务      │◄──►│  (公网地址)     │
│                 │    │                  │    │                 │
│  127.0.0.1:8000 │    │   安全桥接       │    │ https://xxx.com │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        ▲                        ▲                        ▲
        │                        │                        │
   您的本地                    库魔法                   互联网
   应用程序                     ✨                      访问
```

```bash
pip install yanghao.portlink
```

---

## 🚀 快速入门

1.  **安装**
    ```bash
    pip install yanghao.portlink
    ```

2.  **编程方式使用**

    ```python
    from yanghao.portlink import PortLinkClient as Client

    async def main():
        # 将本地8000端口映射到公网, 具体公网地址查看输出的调试信息
        async with Client(8000) as c:
            await c.link(8000)

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
    ```

3.  **Google Colab 示例**

    对于 Google Colab 用户，请查看我们的 [Colab 示例](examples/colab.py)，演示如何将 Gradio 应用暴露到公网。

---

## ✨ 特性

-   **零配置** – 简单易用
-   **TCP 协议** – 简单可靠
-   **自动重连** – 网络中断后可自动恢复
-   **跨平台** – 支持 Linux、macOS、Windows

---

## 🤝 贡献

1.  Fork 本仓库
2.  `pip install -e ".[dev]"`
3.  `pytest` (要求覆盖率 ≥ 90 %)
4.  发起一个 PR

---

## 📄 许可证

MIT © 2025 yahao333

---

## 💬 帮助

-   `https://github.com/yahao333/portlink/discussions`
-   `https://github.com/yahao333/portlink/issues`