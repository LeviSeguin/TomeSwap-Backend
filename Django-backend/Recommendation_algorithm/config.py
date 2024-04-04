#Recommendation_algorithm/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    backend_name: str = "book-recommender-api"
    backend_port: int = 5173
    backend_host: str = "localhost"
