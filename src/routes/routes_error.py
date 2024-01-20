from flask import Blueprint, render_template, flash, request, redirect, url_for, make_response

error_bp = Blueprint('routes_error', __name__)


@error_bp.app_errorhandler(404)
def ruta_desconocida(error):
    response = make_response({"msj": f"Ruta desconocida {error}"}, 404)
    response.headers['Content-Type'] = 'application/json'
    return response
