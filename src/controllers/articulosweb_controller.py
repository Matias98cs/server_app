from src.models.entities import ArticulosWeb, CategoriaWeb, Ofertas


class controller_articulosweb():
    def __init__(self):
        super().__init__()

    def obtener_articulos_search(self, search):
        query = ArticulosWeb.query

        query = query.filter(
            ArticulosWeb.descripcion.ilike(f"%{search}%"))

        return query
