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

    response = make_response({"articulos": articulos_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@articulos_web_bp.route('/articulosweb-search', methods=['GET'])
def obtener_art_search():
    parametros = request.args
    search = parametros.get('s')

    if search is None:
        return {'mensaje': f"Debe ingresar el parametros 's' para buscar el articulo/s"}, 400

    articulos_search = controller_articulosweb().obtener_articulos_search(search)
    articulo_data = []
    for art in articulos_search:
        at = art.serialize()
        articulo_data.append(at)

    response = make_response({"articulo": articulo_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@articulos_web_bp.route('/articulos-web/<search>', methods=['GET'])
def obtener_articulo_query(search):
    if not search:
        response = make_response(
            {"msj": 'Debe ingresa un nombre o descripcion para buscar el articulo'}, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    articulos_search = controller_articulosweb().obtener_articulos_search(search)
    articulo_data = []
    for art in articulos_search:
        at = art.serialize()
        articulo_data.append(at)

    response = make_response({"articulo": articulo_data}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@articulos_web_bp.route('/articulos-web-home', methods=['GET'])
def obtener_art_home():
    articulos = controller_articulosweb().obtener_art_home()
    articulos_serializados = [
        {'descripcion': item.descripcion,
         'foto': item.foto,
         'precio': item.precio,
         'id': item.id} for item in articulos]

    response = make_response({"articulos": articulos_serializados}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@articulos_web_bp.route('/articulosweb-paginado', methods=['GET'])
def obtener_art_paginado():
    pagina = request.args.get('pagina', type=int)
    # cantidad_art = request.args.get('cantidad_art', type=int)

    # if not all([pagina, cantidad_art]):
    if not pagina:
        response = make_response(
            {"msj": 'Debe especificar en los parametros pagina y cantidad_art'}, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    articulos, total_paginas = controller_articulosweb().obtener_por_pagina(
        pagina)

    articulos_data = []
    for art in articulos:
        at = art.serialize()
        articulos_data.append(at)

    response = make_response(
        {"articulos": articulos_data, "total_paginas": total_paginas}, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
