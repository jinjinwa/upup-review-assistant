from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./community_dev.sqlite"
    redis_url: str = "redis://localhost:16379/0"
    celery_broker_url: str = "redis://localhost:16379/1"
    celery_result_backend: str = "redis://localhost:16379/2"
    jwt_secret_key: str = "change-me-community-demo-secret-32-bytes-minimum"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 1440
    demo_admin_email: str = "admin@example.com"
    demo_admin_password: str = "admin123456"
    demo_user_email: str = "demo@example.com"
    demo_user_password: str = "demo123456"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
