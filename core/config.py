# Here is where all configurations are maintained for this Application

# Import Environment Variables in Config.py file
import os
from pathlib import Path
from dotenv import load_dotenv

# Environment Path - Current Folder Check
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    """We are going to keep track of Project in this Class"""
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # Default Postgres PORT
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "db_jobboard")
    # Create a Database URL
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


# Create Object of Class
settings = Settings()
