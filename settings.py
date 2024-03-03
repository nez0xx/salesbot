from pydantic_settings import BaseSettings, SettingsConfigDict


class BotCredentials(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    BOT_TOKEN: str


bot_credentials = BotCredentials()
