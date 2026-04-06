# -*- coding: utf-8 -*-
# @Time : 2026/4/5 星期日 11:33
# @Author : Jamie Hong
from langchain.messages import SystemMessage

from src.kelly.config.model_with_tools import model_with_tools


def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }