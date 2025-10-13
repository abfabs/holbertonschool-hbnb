from abc import ABC, abstractmethod


# Abstract base class defining the repository interface for data persistence
class Repository(ABC):
    # Add a new object to the repository
    @abstractmethod
    def add(self, obj):
        pass


    # Retrieve an object by its unique identifier
    @abstractmethod
    def get(self, obj_id):
        pass


    # Retrieve all objects from the repository
    @abstractmethod
    def get_all(self):
        pass


    # Update an object's data by its unique identifier
    @abstractmethod
    def update(self, obj_id, data):
        pass


    # Delete an object from the repository by its unique identifier
    @abstractmethod
    def delete(self, obj_id):
        pass


    # Retrieve an object by matching a specific attribute value
    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass



# In-memory implementation of the repository using a dictionary for storage
class InMemoryRepository(Repository):
    # Initialize the repository with an empty storage dictionary
    def __init__(self):
        self._storage = {}


    # Add a new object to the repository using its ID as the key
    def add(self, obj):
        self._storage[obj.id] = obj


    # Retrieve an object by its unique identifier
    def get(self, obj_id):
        return self._storage.get(obj_id)


    # Retrieve all objects from the repository as a list
    def get_all(self):
        return list(self._storage.values())


    # Update an object's data if it exists in the repository
    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)


    # Delete an object from the repository if it exists
    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]


    # Retrieve the first object matching the specified attribute value
    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
