from flask import Blueprint, make_response
# from src.controllers.articulosweb_controller import controller_articulosweb
from src.models.entities import Promocion

promociones_bp = Blueprint('routes_promociones', __name__)


@promociones_bp.route('/promociones', methods=['GET'])
def obtener_promociones():
    promociones = Promocion.obtener_todo()
    promociones_data = []
    for promo in promociones:
        pr = promo.serialize()
        promociones_data.append(pr)

    response = make_response({"promociones": promociones_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
