# -*- coding: utf-8 -*-
# @Time : 2026/4/5 星期日 11:32
# @Author : Jamie Hong
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int