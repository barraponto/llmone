from groq import Groq
from openai import OpenAI

from models.config import Config, GroqModel, OpenaiModel

openai_reasoning_token_allowance: dict[OpenaiModel, int] = {
    OpenaiModel.GPT_5: 20 * 1024,
    OpenaiModel.GPT_5_MINI: 10 * 1024,
    OpenaiModel.GPT_5_NANO: 5 * 1024,
}


class Inference:
    def __init__(self, config: Config):
        self.model = config.model
        if self.model in GroqModel:
            self.client = Groq(api_key=config.groq_api_key)
        elif self.model in OpenaiModel:
            self.client = OpenAI(api_key=config.openai_api_key)

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a gay helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            **self._provider_specific_kwargs(),
        )

        if response.choices[0].finish_reason == "length":
            return "I'm sorry, just thinking about it makes my head hurt. Please try something simpler."

        return response.choices[0].message.content

    def _provider_specific_kwargs(self) -> dict:
        if self.model in GroqModel:
            return {"temperature": 0.7, "max_tokens": 2048}
        elif self.model in OpenaiModel:
            return {
                "reasoning_effort": "low",
                "max_completion_tokens": 2048
                + openai_reasoning_token_allowance[self.model],
            }
