from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date
from sqlalchemy.orm import sessionmaker


def cadastrar(nome, cpf, data_nasc, email, senha):

    cpf = int(cpf)

    engine = create_engine(CONNECTION_STRING, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()

    class User(Base):
        __tablename__ = 'FoodFinderUser'

        Nome = Column(String(255))
        CPF = Column(BigInteger, primary_key=True)
        Data_Nasc = Column(String(255))
        Email = Column(String(255))
        Senha = Column(String(255))

    Base.metadata.create_all(engine)
    ffUser = User(Nome=nome, CPF=cpf, Data_Nasc=data_nasc, Email=email, Senha=senha)
    session.add(ffUser)
    session.commit()
    session.close()
    success = "Cadastro concluido com sucesso!"

    return success
