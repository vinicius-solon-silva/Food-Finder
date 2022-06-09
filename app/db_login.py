from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String
from sqlalchemy.orm import sessionmaker


engine = create_engine(f'mssql+pymssql://adminvinicius:vinnyadmin123!@viniciussilva-sv.database.windows.net:1433/viniciussilva-db', echo=False)
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
            return true
        else:
            session.commit()
            session.close() 
            return "Nao foi possivel fazer login, tente novamente."
    except Exception as e:
        session.commit()
        session.close() 
        return "Cadastro inexistente no banco, consulte o desenvolvedor!\nCodigo do erro: " + e
