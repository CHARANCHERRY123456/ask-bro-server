import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    # postgresql database
    DB_URL: str = os.getenv("DB_URL", "postgresql://user:password@localhost/dbname")


settings = Settings()

