from project.app.repositories.reactor_repository import ReactorNoRelationalRepository

class ReactorService:
    def __init__(self):
        self.repository = ReactorNoRelationalRepository()
        
    # 1. Obtener reactores registrados
    def get_all_reactors(self):
        return self.repository.get_all_reactors()

    # 2. Obtener un reactor por Id
    def get_reactor_by_id(self, id: str):
        return self.repository.get_reactor_by_id(id)
    
    def get_all_reactor_types(self):
        return self.repository.get_all_reactor_types()

    def get_all_locations(self):
        return self.repository.get_all_locations()

    def get_reactors_with_same_reactor_type_by_id(self, reactor_id: int):
        return self.repository.get_reactors_with_same_reactor_type_by_id(reactor_id)
    
    def get_reactors_with_same_location_by_id(self, reactor_id:int):
        return self.repository.get_reactors_with_same_location_by_id(reactor_id)
    
    def get_reactors_by_location(self, country: str, city: str):
        return self.repository.get_reactors_by_location(country, city)
    
    # 3. Crear un nuevo reactor. #LISTO
    def create_reactor(self, reactor: dict):
        return self.repository.create_reactor(reactor)
    
    # 4. Actualizar un reactor existente. #LISTO
    def update_reactor(self, reactor: dict, reactor_id: str):
        return self.repository.update_reactor(reactor, reactor_id)
    
    # 5. Eliminar un reactor existente. #LISTO
    def delete_reactor_by_id(self, reactor_id: str):
        return self.repository.delete_reactor_by_id(reactor_id)
    
