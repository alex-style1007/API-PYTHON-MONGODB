from pydantic import BaseModel
from typing import Union
from datetime import datetime


class ReactorResponseModel(BaseModel):
    id:                         int
    nombre:                     str
    potencia_termica:           float
    primera_fecha_reaccion:     Union[datetime, None]
    tipo:                       Union[str, None]
    estado:                     str
    ciudad:                     Union[str, None]
    pais:                       str

class ReactorTypeResponseModel(BaseModel):
    id:                         int
    tipo:                       str

class LocationResponseModel(BaseModel):
    ciudad:                     Union[str, None]
    pais:                       str

class ReactorCreateModel(BaseModel):
    nombre:                     str
    potencia_termica:           float
    primera_fecha_reaccion:     Union[datetime, None]
    tipo:                       Union[str, None]
    estado:                     str
    ciudad:                     Union[str, None]
    pais:                       str