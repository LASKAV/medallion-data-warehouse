from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import urlparse


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    pg_dsn: PostgresDsn = Field(alias="DATABASE_URL_DOCKER")

    def get_jdbc_options(self):
        """Return dict with JDBC options for Spark."""
        parsed = urlparse(str(self.pg_dsn))
        return {
            "url": f"jdbc:postgresql://{parsed.hostname}:{parsed.port}{parsed.path}",
            "user": parsed.username,
            "password": parsed.password,
        }


settings = Settings()
