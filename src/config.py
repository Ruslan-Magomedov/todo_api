from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ Переменные окружения """
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    model_config = SettingsConfigDict(env_file=".env")

    @property
    def db_url(self) -> str:
        """ Ссылка на подключение к базе данных postgresql """
        return f"postgresql+asyncpg://{self.DB_NAME}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
