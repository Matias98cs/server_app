from src.models.entities import ArticulosWeb


class controller_articulosweb():
    def __init__(self):
        super().__init__()

    def obtener_con_filtro(self, descripcion):
        query = ArticulosWeb.query

        if descripcion:
            query = query.filter(
                ArticulosWeb.descripcion.ilike(f"%{descripcion}%"))

        return query.all() if descripcion else []
