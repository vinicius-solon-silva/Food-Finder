from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String
from sqlalchemy.orm import sessionmaker
from AUTH import CONN_STR


engine = create_engine(CONN_STR, echo=False)
Base = declarative_base()
class User(Base):
    __tablename__ = 'FoodFinderUser'
    Nome = Column(String(255))
    CPF = Column(BigInteger, primary_key=True)
    Data_Nasc = Column(String(255))
    Email = Column(String(255))
    Senha = Column(String(255))
Base.metadata.create_all(engine)
Sessions = sessionmaker(bind=engine)
session = Sessions()


def login(cpf, senha):
    cpf = int(cpf)
    try:
        query = session.query(User).filter(User.CPF == cpf).first()
        login = query.CPF
        passwd = query.Senha     
        if login and passwd == senha:
            session.commit()
            session.close()   
            return True
        else:
            session.commit()
            session.close() 
            return "Nao foi possivel fazer login, tente novamente."
    except Exception as e:
        session.commit()
        session.close() 
        return "Cadastro inexistente no banco, consulte o desenvolvedor!\nCodigo do erro: " + e
