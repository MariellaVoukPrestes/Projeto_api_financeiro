
from sqlalchemy import create_engine

DATABASE_NAME = "dados.db"

def get_engine_sqlite():
    engine = create_engine(f"sqlite:///{DATABASE_NAME}")
    return engine