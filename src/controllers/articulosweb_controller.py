from src.models.entities import ArticulosWeb
from config import registros_por_pagina


class controller_articulosweb():
    def __init__(self):
        super().__init__()

    def obtener_articulos_search(self, search):
        query = ArticulosWeb.query

        query = query.filter(
            ArticulosWeb.descripcion.ilike(f"%{search}%"))

        return query

    def obtener_art_home(self):
        query = ArticulosWeb.query.with_entities(
            ArticulosWeb.descripcion, ArticulosWeb.foto, ArticulosWeb.precio, ArticulosWeb.id)
        return query

    def obtener_por_pagina(self, pagina=1):
        query = ArticulosWeb.query
        print(type(registros_por_pagina))
        articulos, pagina = ArticulosWeb.obtener_paginado(
            query, pagina, registros_por_pagina)
        return articulos, pagina
