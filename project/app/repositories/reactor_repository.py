from project.app.context.db_connection import MongoDB
from project.app.models.reactor import Reactor, Ubicacion, Estado, TipoReactor, Pais
from bson.objectid import ObjectId

class ReactorNoRelationalRepository:

    def __init__(self):
        self.mongodb = MongoDB()

    # 1. Obtener reactores registrados #LISTO
    def get_all_reactors(self):
        return self.get_full_reactor_document()

    # 2. Obtener un reactor por Id
    def get_reactor_by_id(self, id: int):
        full_query = self.get_full_query()
        result = full_query.filter(Reactor.id == id).first()
        if result is not None:
            return {
                **self.model_as_dict(result[0]),
                'estado': result[1],
                'ciudad': result[2],
                'pais': result[3],
                'tipo': result[4]
            }
        return {'message': f'El reactor con id {id} no existe'}

    # 3. Crear un nuevo reactor. #LISTO
    def create_reactor(self, reactor: dict):
        reactor_item = self.get_reactor_objectid_references(reactor)
        collection = self.mongodb._get_collection('reactoresdb', 'reactores')
        collection.insert_one(reactor_item)
        return {'message': 'El reactor ha sido insertado con éxito'}
    
    # 4. Actualizar un reactor existente. #LISTO
    def update_reactor(self, reactor: dict, reactor_id: str):
        reactor_item = self.get_reactor_objectid_references(reactor)
        collection = self.mongodb._get_collection('reactoresdb', 'reactores')
        old_reactor = collection.find_one({'_id': ObjectId(reactor_id)})
        if old_reactor is None:
            return {'message': f'El reactor con id {reactor_id} no existe'} 
        collection.update_one({'_id': ObjectId(reactor_id)}, {'$set': reactor_item})
        return {'message': f'el reactor con id {reactor_id} fue actualizado con éxito',
                'reactor': {"id":reactor_id, **reactor}}
    
    # 5. Eliminar un reactor existente. #LISTO
    def delete_reactor_by_id(self, id: str):
        collection = self.mongodb._get_collection('reactoresdb', 'reactores')
        reactor = collection.find_one({'_id': ObjectId(id)})
        if reactor is not None:
            collection.delete_one({'_id': ObjectId(id)})
            return {'message': f'El reactor con id {id} fue eliminado con éxito'}
        return {'message': f'El reactor con id {id} no existe'}
    
    # 6. Obtener tipos de reactores registrados #LISTO
    def get_all_reactor_types(self):
        collection = self.mongodb._get_collection('reactoresdb', 'tipos_reactor')
        results = collection.find()
        response = []
        for item in results:
            item['id'] = str(item['_id'])
            response.append(item)
        return response

    # 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo.
    def get_reactors_with_same_reactor_type_by_id(self, reactor_id:int):
        reactor = self.session.query(TipoReactor.id).join(
            Reactor, 
            TipoReactor.id == Reactor.id_tipo_reactor,
            isouter=True
            ).filter(Reactor.id == reactor_id).first()
        if reactor is None:
            return {'message': f'El reactor con id {reactor_id} no existe'}
        full_query = self.get_full_query()
        results = full_query.filter(Reactor.id_tipo_reactor == reactor[0]).all()
        response = []
        for result in results:
            response.append(
                {
                    **self.model_as_dict(result[0]),
                    'estado': result[1],
                    'ciudad': result[2],
                    'pais': result[3],
                    'tipo': result[4]
                }
            )
        return response
    
    # 8. Obtener Ubicaciones Registradas #LISTO
    def get_all_locations(self):
        collection = self.mongodb._get_collection('reactoresdb', 'ubicaciones')
        results = collection.find()
        response = []
        for item in results:
            if 'ciudad' not in item.keys():
                item['ciudad'] = 'Sin asignar'
            item['id'] = str(item['_id'])
            response.append(item)
        return response
    
    # 9. Obtener Ubicación por Id.
    def get_reactors_with_same_location_by_id(self, reactor_id:int):
        reactor = self.session.query(Ubicacion.id).join(
            Reactor, 
            Ubicacion.id == Reactor.id_ubicacion,
            isouter=True
            ).filter(Reactor.id == reactor_id).first()
        if reactor is None:
            return {'message': f'El reactor con id {reactor_id} no existe'}
        full_query = self.get_full_query()
        results = full_query.filter(Reactor.id_ubicacion == reactor[0]).all()
        response = []
        for result in results:
            response.append(
                {
                    **self.model_as_dict(result[0]),
                    'estado': result[1],
                    'ciudad': result[2],
                    'pais': result[3],
                    'tipo': result[4]
                }
            )
        return response
    
    # 10. Obtener Reactores registrados por Ubicación
    def get_reactors_by_location(self, country: str, city: str):
        where_conditions = self.get_where_location_conditions(country, city)

        if len(where_conditions) > 0:
            full_query = self.get_full_query()
            results = full_query.filter(*where_conditions).all()
            response = []
            for result in results:
                response.append(
                    {
                        **self.model_as_dict(result[0]),
                        'estado': result[1],
                        'ciudad': result[2],
                        'pais': result[3],
                        'tipo': result[4]
                    }
                )
            return response
        return self.get_all_reactors()
    

    # Funciones Auxiliares
    def get_reactor_objectid_references(self, reactor: dict):
        locations_collection = self.mongodb._get_collection('reactoresdb', 'ubicaciones')
        reactor_types_collection = self.mongodb._get_collection('reactoresdb', 'tipos_reactor')
        reactor_type = reactor_types_collection.find_one({'tipo': reactor['tipo']})
        location = locations_collection.find_one({'ciudad': reactor['ciudad'], 'pais': reactor['pais']})
        if reactor_type is None:
            new_reactor_type = {'tipo': reactor['tipo']}
            reactor_types_collection.insert_one(new_reactor_type)
            reactor_type = new_reactor_type
        if location is None:
            new_location = {'ciudad': reactor['ciudad'], 'pais': reactor['pais']}
            locations_collection.insert_one(new_location)
            location = new_location
        reactor_item = {
            'nombre': reactor['nombre'],
            "potencia_termica": reactor['potencia_termica'],
            "primera_fecha_reaccion": reactor['primera_fecha_reaccion'],
            "estado": reactor['estado'],
            "tipo_reactor_id": reactor_type['_id'],
            "ubicacion_id": location['_id']

        }
        return reactor_item
    

    def get_full_reactor_document(self):
        reactors_collection = self.mongodb._get_collection('reactoresdb', 'reactores')
        full_reactors_documents = reactors_collection.aggregate([
            {"$lookup": {"from": "tipos_reactor", "localField": "tipo_reactor_id", "foreignField": "_id", "as": "info_tipo_reactor"}},
            {"$lookup": {"from": "ubicaciones", "localField": "ubicacion_id", "foreignField": "_id", "as": "ubicacion"}},
            {"$unwind": "info_tipo_reactor"},
            {"$unwind": "ubicacion"},
            {"$addFields": {"tipo_reactor": "$info_tipo_reactor.tipo", "pais": "$ubicacion.pais", "ciudad": "$ubicacion.ciudad"}},
            {"$project": {"nombre": 1, "potencia_termica":1, "estado":1, "tipo_reactor":1, "pais":1, "ciudad":1  }}
        ])
        return [document for document in full_reactors_documents]

    


    def get_where_location_conditions(self, country: str, city: str):
        where_conditions = []
        if country:
            where_conditions.append(
                Pais.pais == country
            )
        if city:
            where_conditions.append(
                Ubicacion.ciudad == city
            )
        return where_conditions
    

    # Funcion para transformar objeto de un modelo a diccionario 
    def model_as_dict(self, object):
        return {attr.key: getattr(object, attr.key) for attr in object.__mapper__.attrs}
