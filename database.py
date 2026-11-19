from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string: PostgreSQL on RDS when deployed, SQLite as the fallback
# for local runs and for the CI job (where DATABASE_URL is not set)
DATABASE_URL = environ.get("DATABASE_URL", "sqlite:///./test.db")

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our models
Base = declarative_base()
