from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="FastAPI Full Stack Project")
    VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=True)
    
    # Database
    DATABASE_URL: str = Field(default="sqlite:///./test.db")
    TEST_DATABASE_URL: str = Field(default="sqlite:///./test_test.db")
    
    # JWT
    SECRET_KEY: str = Field(default="your-secret-key-change-this-in-production")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    
    # CORS
    ALLOWED_HOSTS: List[str] = Field(default=["*"])
    
    # Email
    SMTP_TLS: bool = Field(default=True)
    SMTP_PORT: int = Field(default=587)
    SMTP_HOST: str = Field(default="")
    SMTP_USER: str = Field(default="")
    SMTP_PASSWORD: str = Field(default="")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
