from pydantic import (
    BaseSettings,
    PostgresDsn,
    Field,
)



class Settings(BaseSettings):    
    pg_dsn: PostgresDsn = Field(..., env='DATABASE_URL_CAR')
    car_name: str = 'Valmet-service'
    bot_token: str = Field(..., env='CAR_HOLDER_TOKEN')
    logger_level: str = Field(..., env='CAR_HOLDER_LOGGER_LEVEL')
    allowed_change_city: list = (400501317,)

settings = Settings()
