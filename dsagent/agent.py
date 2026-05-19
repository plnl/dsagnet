class DsAgent:
    """A simple dsagent helper class."""

    def process(self, prompt: str) -> str:
        if not prompt.strip():
            return "请提供一个有效的 prompt。"
        return f"已收到请求：{prompt}. 这是一个简单的 dsagent 响应示例。"
