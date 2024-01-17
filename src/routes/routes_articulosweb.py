from flask import Blueprint, render_template, flash, request, redirect, url_for, make_response
from src.controllers.articulosweb_controller import controller_articulosweb
from src.models.entities import ArticulosWeb
import json

articulos_web_bp = Blueprint('routes_articulosweb', __name__)


@articulos_web_bp.route('/articulosweb', methods=['GET'])
def obtener_articulosweb():
    articulos = ArticulosWeb.obtener_todo()
    articulos_data = []
    for art in articulos:
        at = art.serialize()
        articulos_data.append(at)

    return {'articulos': articulos_data}, 200


@articulos_web_bp.route('/articuloswebsearch', methods=['GET'])
def obtener_art_search():
    parametros = request.args
    categoria = parametros.get('categoria')
    search = parametros.get('s')
    rangoregistros = parametros.get('rangoregistros')
    sucursal = parametros.get('sucursal')
    ofertas = parametros.get('ofertas')

    if not search:
        return {'mensaje': "Debe ingresar el parametros 's' para buscar el articulo"}, 400

    articulos_search = controller_articulosweb().obtener_con_filtro(search)
    articulo_data = []
    for art in articulos_search:
        at = art.serialize()
        articulo_data.append(at)

    return {'articulo': articulo_data}
