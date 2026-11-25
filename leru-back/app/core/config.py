from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://leruaitte:leruaitte@localhost:5432/leruaitte"
    jwt_secret_key: str = "troque-esta-chave-secreta-em-producao"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    cors_origins: list[str] = ["http://localhost:5173"]


settings = Settings()
