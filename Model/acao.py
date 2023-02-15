from sqlalchemy import Column, Integer, String, Float, DateTime
from Model.engine_sqlalchemy import Base, session
import datetime


class Acao(Base):
    __tablename__ = 'acao'
    def __init__(self,  ticket, nome_empresa, cotacao, dividend_ano_0, dividend_ano_1, dividend_ano_2, dividend_ano_3, dividend_ano_4, created_at=None, updated_at=None, deleted_at=None):
        self.ticket = ticket
        self.nome_empresa = nome_empresa
        self.cotacao = cotacao
        self.dividend_ano_0 = dividend_ano_0
        self.dividend_ano_1 = dividend_ano_1
        self.dividend_ano_2 = dividend_ano_2
        self.dividend_ano_3 = dividend_ano_3
        self.dividend_ano_4 = dividend_ano_4
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket = Column(String(8), nullable=False)
    nome_empresa = Column(String(200), nullable=True)
    cotacao = Column(Float(2), nullable=True)
    dividend_ano_0 = Column(Float(2), nullable=True)
    dividend_ano_1 = Column(Float(2), nullable=True)
    dividend_ano_2 = Column(Float(2), nullable=True)
    dividend_ano_3 = Column(Float(2), nullable=True)
    dividend_ano_4 = Column(Float(2), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now())
    updated_at = Column(DateTime, nullable=True, default=None)
    deleted_at = Column(DateTime, nullable=True, default=None)


    def add_update(acao):
        acao_update = session.query(Acao).filter(Acao.ticket == acao.ticket).first()
        if acao_update:
            if acao.ticket == acao_update.ticket and acao.nome_empresa == acao_update.nome_empresa and acao.cotacao == acao_update.cotacao and acao.dividend_ano_0 == acao_update.dividend_ano_0 and acao.dividend_ano_1 == acao_update.dividend_ano_1 and acao.dividend_ano_2 == acao_update.dividend_ano_2 and acao.dividend_ano_3 == acao_update.dividend_ano_3 and acao.dividend_ano_4 == acao_update.dividend_ano_4:
                return "A ação não teve alteração"
            else:
                acao_update.ticket = acao.ticket
                acao_update.nome_empresa = acao.nome_empresa
                acao_update.cotacao = acao.cotacao
                acao_update.dividend_ano_0 = acao.dividend_ano_0
                acao_update.dividend_ano_1 = acao.dividend_ano_1
                acao_update.dividend_ano_2 = acao.dividend_ano_2
                acao_update.dividend_ano_3 = acao.dividend_ano_3
                acao_update.dividend_ano_4 = acao.dividend_ano_4
                acao_update.updated_at = datetime.datetime.now()
                session.commit()
                return "Ação adicionada com sucesso"
        else:
            acao.created_at = datetime.datetime.now()
            session.add(acao)
            session.commit()
            return "Ação adicionada com sucesso"
        

    def read():
        return session.query(Acao).all()

    def read_especific(ticket):
        return session.query(Acao).filter(Acao.ticket == ticket).first()

    def list_all():
        acoes = session.query(Acao).all()
        acoes_formated = []
        for acao in acoes:
            acoes_formated.append({
                "ticket" : acao.ticket,
                "nome_empresa" : acao.nome_empresa,
                "cotacao" : acao.cotacao,
                "dividend_ano_0" : acao.dividend_ano_0,
                "dividend_ano_1" : acao.dividend_ano_1,
                "dividend_ano_2" : acao.dividend_ano_2,
                "dividend_ano_3" : acao.dividend_ano_3,
                "dividend_ano_4" : acao.dividend_ano_4
            })

        return acoes_formated
