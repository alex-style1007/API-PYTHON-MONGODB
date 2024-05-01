from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TipoReactor(BaseModel):
    id: int
    tipo: str

    class Config:
        orm_mode = True
        collection = "tipos_reactor"

class Pais(BaseModel):
    id: int
    pais: str

    class Config:
        orm_mode = True
        collection = "paises"

class Ubicacion(BaseModel):
    id: int
    ciudad: Optional[str]
    pais_id: int

    class Config:
        orm_mode = True
        collection = "ubicacion"

class Estado(BaseModel):
    id: int
    estado: str

    class Config:
        orm_mode = True
        collection = "estados"

class Reactor(BaseModel):
    id: int
    nombre: str
    potencia_termica: float
    primera_fecha_reaccion: Optional[datetime]
    tipo_reactor_id: int
    ubicacion_id: int
    estado_id: int

    class Config:
        orm_mode = True
        collection = "reactores"
