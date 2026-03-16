from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database Configuration
    db_host: str = Field(..., env='DB_HOST')
    db_port: int = Field(..., env='DB_PORT')
    db_user: str = Field(..., env='DB_USER')
    db_password: str = Field(..., env='DB_PASSWORD')
    db_name: str = Field(..., env='DB_NAME')

    # Kafka Configuration
    kafka_broker: str = Field(..., env='KAFKA_BROKER')
    kafka_topic: str = Field(..., env='KAFKA_TOPIC')

    # Redis Configuration
    redis_host: str = Field(..., env='REDIS_HOST')
    redis_port: int = Field(..., env='REDIS_PORT')

    # LLM Configuration
    llm_api_key: str = Field(..., env='LLM_API_KEY')
    llm_model: str = Field(..., env='LLM_MODEL')

    # Feature Flags
    feature_flags: dict = Field(default_factory=dict, env='FEATURE_FLAGS')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()