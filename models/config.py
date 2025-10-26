from dataclasses import dataclass
from enum import StrEnum


class GroqModel(StrEnum):
    GROQ_LLAMA_3_1_8B_INSTANT = "llama-3.1-8b-instant"
    GROQ_GPT_OSS_20B = "openai/gpt-oss-20b"


class OpenaiModel(StrEnum):
    GPT_5 = "gpt-5"
    GPT_5_MINI = "gpt-5-mini"
    GPT_5_NANO = "gpt-5-nano"


model_choices = [str(value) for value in GroqModel] + [
    str(value) for value in OpenaiModel
]


@dataclass
class Config:
    groq_api_key: str
    openai_api_key: str
    model: GroqModel | OpenaiModel
