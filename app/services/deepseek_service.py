# services/deepseek_service.py

from openai import OpenAI

# 初始化 OpenAI 客户端，设置 DeepSeek API 的 base_url 和您的 API 密钥
client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.deepseek.com")


def get_deepseek_response(messages: list, model: str = "deepseek-chat") -> str:
    """
    调用 DeepSeek API 获取模型回复。

    :param messages: 对话消息列表，包含用户和系统的消息
    :param model: 使用的模型名称，默认为 'deepseek-chat'
    :return: 模型的回复内容
    """
    response = client.chat.completions.create(
        model=model, messages=messages, stream=False
    )
    return response.choices[0].message.content
