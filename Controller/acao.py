from flask import Blueprint, request
from Model.fundamentus_acoes import pegar_acoes_fundamentus
from Model.acao import Acao


blueprint_acao = Blueprint("blueprint_acao", __name__)


@blueprint_acao.route("/list_all", methods=["GET"])
def list_all():
    acoes = Acao.list_all()
    return acoes