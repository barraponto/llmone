from groq import Groq

from models.config import LLModel


class Inference:
    def __init__(self, api_key: str, model: LLModel):
        self.api_key = api_key
        self.model = model
        self.client = Groq(api_key=api_key)

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=1024,
            messages=[
                {"role": "system", "content": "You are a gay helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
