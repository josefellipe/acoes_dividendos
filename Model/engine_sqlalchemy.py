from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///b3_fundamentus.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def executar_mudancas_bd():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print("Erro ao criar tabelas: ", e)