from typing import List, Union
from fastapi import FastAPI, status, Path, Query, Body
from project.app.models.reactor_schema import ReactorResponseModel, ReactorTypeResponseModel, LocationResponseModel, ReactorCreateModel, NotExistingReactorId
from project.app.services.reactor_service import ReactorService
from project.app.exceptions.exceptions import Exceptions

app = FastAPI()

app.add_exception_handler(Exception, handler=Exceptions().base_error)

# 1. Obtener reactores registrados #PENSAR

@app.get(
        path='/reactors',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactors():
    return ReactorService().get_all_reactors()

# 6. Obtener tipos de reactores registrados. #LISTO
@app.get(
        path='/reactors/types',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorTypeResponseModel],
)
async def get_all_reactor_types():
    return ReactorService().get_all_reactor_types()

# 8. Obtener Ubicaciones Registradas. #LISTO
@app.get(
        path='/reactors/locations',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationResponseModel],
)
async def get_all_locations():
    return ReactorService().get_all_locations()

# 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo. #PENSAR
@app.get(
        path='/reactors/types/{id}',
        status_code=status.HTTP_200_OK,
        response_model=Union[List[ReactorResponseModel], NotExistingReactorId],
)
async def get_reactors_with_same_reactor_type_by_id(id: str):
    return ReactorService().get_reactors_with_same_reactor_type_by_id(id)

# 10. Obtener Reactores registrados por Ubicación #PENSAR
@app.get(
        path='/reactors/location',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactors_by_location(country: str = Query(default=None), city: str = Query(default=None)):
    return ReactorService().get_reactors_by_location(country, city)

# 9. Obtener Ubicación por Id. #PENSAR
@app.get(
        path='/reactors/location/{id}',
        status_code=status.HTTP_200_OK,
        response_model=Union[List[ReactorResponseModel], NotExistingReactorId],
)
async def get_reactors_with_same_location_by_id(id: str):
    return ReactorService().get_reactors_with_same_location_by_id(id)

# 2. Obtener un reactor por Id. #TALVES
@app.get(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
        response_model=Union[ReactorResponseModel, NotExistingReactorId]
)
async def get_reactor_by_id(id: str):
    return ReactorService().get_reactor_by_id(id)

# 3. Crear un nuevo reactor. #LISTO
@app.post(
        path='/reactors',
        status_code=status.HTTP_201_CREATED,
)
async def create_reactor(reactor: ReactorCreateModel=Body(...)):
    return ReactorService().create_reactor(reactor.model_dump())

# 4. Actualizar un reactor existente. #LISTO
@app.put(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
)
async def update_reactor(reactor: ReactorCreateModel=Body(...), id: str = Path(...)):
    return ReactorService().update_reactor(reactor.model_dump(), id)

# 5. Eliminar un reactor existente. #LISTO
@app.delete(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
)
async def delete_reactor_by_id(id: str = Path(...)):
    return ReactorService().delete_reactor_by_id(id)
