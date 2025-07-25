from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_host: str = ''
    app_port: int = 5000
    gemini_api_key: str = ''
    open_api_key: str = ''
    database_url: str = ''
    jwt_secret_key: str = ''

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
