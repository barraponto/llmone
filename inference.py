from groq import Groq


class Inference:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.client = Groq(api_key=api_key)

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=256,
            messages=[
                {"role": "system", "content": "You are a gay helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
