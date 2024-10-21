from sqlalchemy import create_engine
from sqlalchemy.orm import sesssionmaker
from contextlib import contextmanager

# URL de conexão para BD MySQL
DATABASE_URL = f"mysql+pymysql://ususario:senha@host:porta/nome_bd"