from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from Model.engine_sqlalchemy import executar_mudancas_bd
from Model.fundamentus_acoes import pegar_acoes_fundamentus
from flask import Flask
from Model.acao import Acao
from Controller.acao import blueprint_acao


def iniciar_agendamento():
    scheduler = BackgroundScheduler(timezone=pytz.timezone("America/Sao_Paulo"))
    scheduler.add_job(pegar_acoes_fundamentus, 'cron', hour='1', timezone=pytz.timezone("America/Sao_Paulo"))
    scheduler.start()



if __name__ == "__main__":
    executar_mudancas_bd()
    iniciar_agendamento()
    pegar_acoes_fundamentus()
    
    app = Flask(__name__)
    app.register_blueprint(blueprint_acao)
    app.run()
