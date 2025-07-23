from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_host: str
    app_port: int
    gemini_api_key: str
    open_api_key: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
