from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
username = "postgres"
password = "root"
hostname = "localhost"
port = "5432"
DB_URL = "postgresql://postgres:AcademyRootPassword@localhost:5432/api_tutorial_class"
engine = create_engine(DB_URL)
# binding the engine to a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()