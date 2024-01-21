from src.models.entities import ArticulosWeb


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
