from dataclasses import dataclass
from enum import StrEnum


class LLModel(StrEnum):
    GROQ_LLAMA_3_1_8B_INSTANT = "llama-3.1-8b-instant"
    GROQ_GPT_OSS_20B = "openai/gpt-oss-20b"


@dataclass
class Config:
    groq_api_key: str
    model: LLModel
