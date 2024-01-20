from flask import Blueprint, make_response
# from src.controllers.articulosweb_controller import controller_articulosweb
from src.models.entities import CategoriaWeb

categorias_web_bp = Blueprint('routes_categoriasweb', __name__)


@categorias_web_bp.route('/categoriasweb', methods=['GET'])
def obtener_categorias():
    categorias = CategoriaWeb.obtener_todo()
    categorias_data = []
    for art in categorias:
        at = art.serialize()
        categorias_data.append(at)

    response = make_response({"categorias": categorias_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
