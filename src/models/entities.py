import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from src.models.base import BaseEntity, db


class Peticioneservidor(BaseEntity):
    __tablename__ = 'peticioneservidor'
    id = db.Column(db.Integer, primary_key=True)
    instancia = db.Column(db.String)
    estado = db.Column(db.Integer)
    parametro1 = db.Column(db.String)
    parametro2 = db.Column(db.String)
    fechainsercion = db.Column(db.DateTime)
    fecha = db.Column(db.DateTime)
    peticion = db.Column(db.Integer)

    def __init__(self, parametro1, estado, peticion):
        self.parametro1 = parametro1
        self.estado = estado
        self.peticion = peticion


class Documentos(BaseEntity):
    __tablename__ = 'documentos'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(1))
    articulos = db.Column(db.String(255))
    clienteol = db.Column(db.String(255))

    def __init__(self, estado, articulos, clienteol):
        self.estado = estado
        self.articulos = articulos
        self.clienteol = clienteol


class Productos(BaseEntity):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    precio = db.Column(db.Integer)
    descripcion = db.Column(db.String)
    categoria_id = db.Column(db.Integer)


class Categorias(BaseEntity):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)


class Ofertas(BaseEntity):
    __tablename__ = 'ofertas'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    fechadesde = db.Column(db.DateTime)
    fechahasta = db.Column(db.DateTime)
    sucursal = db.Column(db.Integer)
    precio = db.Column(db.Float)
    preciomay = db.Column(db.Float)
    cantidadmayorista = db.Column(db.Integer)


class Promocion(BaseEntity):
    __tablename__ = 'promociones'
    idpromocion = db.Column(db.Integer, primary_key=True)
    regla1 = db.Column(db.String(255))
    regla2 = db.Column(db.String(255))
    porcentaje = db.Column(db.Integer)
    monto = db.Column(db.Float)
    cantidad1 = db.Column(db.Integer)
    cantidad2 = db.Column(db.Integer)
    nombre = db.Column(db.String(255))
    abv = db.Column(db.String(255), default="")
    orden = db.Column(db.Integer)
    sucursal = db.Column(db.Integer)
    desde = db.Column(db.DateTime)
    hasta = db.Column(db.DateTime)
    martes = db.Column(db.String(1))
    miercoles = db.Column(db.String(1))
    jueves = db.Column(db.String(1))
    viernes = db.Column(db.String(1))
    sabado = db.Column(db.String(1))
    domingo = db.Column(db.String(1))
    tipo = db.Column(db.String(1))
    marca = db.Column(db.Integer)
    codigo = db.Column(db.Integer)


class ArticulosWeb(BaseEntity):
    __tablename__ = 'articulosweb'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    precio = db.Column(db.Float)
    precionormal = db.Column(db.Float)
    descripcion = db.Column(db.String(255))
    presentacion = db.Column(db.String(255))
    pesable = db.Column(db.Boolean)
    pesableporunidad = db.Column(db.Boolean)
    cmax = db.Column(db.Float)
    nombremarca = db.Column(db.String(255))
    marcareal = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
    fraccion = db.Column(db.Integer)
    ppfraccion = db.Column(db.Float)
    coeficiente = db.Column(db.Float)
    preciopor = db.Column(db.Float)
    unidaddmedida = db.Column(db.String(255))
    cantidadmayorista = db.Column(db.Integer)
    preciomayorista = db.Column(db.Float)
    etiquetamedida = db.Column(db.String(255))
    da = db.Column(db.String(255))
    de = db.Column(db.String(255))
    foto = db.Column(db.String(255))
