from pydantic_ai import Agent, ModelSettings
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.providers.groq import GroqProvider
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.models.groq import GroqModel as GroqChatModel

from models.config import Config, GroqModel, OpenaiModel

AGENT_NAME = "LLMOne"
SYSTEM_PROMPT = "You are a gay helpful assistant."

openai_reasoning_token_allowance: dict[OpenaiModel, int] = {
    OpenaiModel.GPT_5: 20 * 1024,
    OpenaiModel.GPT_5_MINI: 10 * 1024,
    OpenaiModel.GPT_5_NANO: 5 * 1024,
}


class Inference:
    @staticmethod
    def get_settings(model: GroqModel | OpenaiModel) -> ModelSettings:
        if model in GroqModel:
            return ModelSettings(temperature=0.7, max_tokens=2048)
        elif model in OpenaiModel:
            return ModelSettings(
                reasoning_effort="low",
                max_completion_tokens=2048 + openai_reasoning_token_allowance[model],
            )

    @staticmethod
    def get_model(
        model: GroqModel | OpenaiModel, config: Config
    ) -> GroqChatModel | OpenAIChatModel:
        model_settings = Inference.get_settings(model)
        if model in GroqModel:
            return GroqChatModel(
                model,
                provider=GroqProvider(api_key=config.groq_api_key),
                settings=model_settings,
            )
        elif model in OpenaiModel:
            return OpenAIChatModel(
                model,
                provider=OpenAIProvider(api_key=config.openai_api_key),
                settings=model_settings,
            )

    def __init__(self, config: Config):
        self.model = config.model
        self.client = Agent(
            model=Inference.get_model(config.model, config),
            system_prompt=SYSTEM_PROMPT,
            name=AGENT_NAME,
            output_type=str,
        )

    def chat(self, prompt: str) -> str:
        result = self.client.run_sync(user_prompt=prompt)

        if result.response.finish_reason == "length":
            return "I'm sorry, just thinking about it makes my head hurt. Please try something simpler."

        return result.output
