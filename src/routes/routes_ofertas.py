from flask import Blueprint, make_response
from src.models.entities import Ofertas

ofertas_bp = Blueprint('routes_ofertas', __name__)


@ofertas_bp.route('/ofertas', methods=['GET'])
def obtener_ofertas():
    ofertas = Ofertas.obtener_todo()
    ofertas_data = []
    for oferta in ofertas:
        oft = oferta.serialize()
        ofertas_data.append(oft)

    response = make_response({"ofertas": ofertas_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
