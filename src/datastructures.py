
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []
        self._next_id = 1  # Inicializamos un contador para IDs únicos.

    def _generateId(self):
        return self._next_id

    def add_member(self, member):
        """
        Agrega un nuevo miembro a la lista de _members. 
        Si no se proporciona un ID, se genera automáticamente.
        """
        if "id" not in member:
            member["id"] = self._generateId()
            self._next_id += 1
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        """
        Elimina un miembro de la familia por su ID.
        """
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        """
        Recupera un miembro de la familia por su ID.
        """
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        """
        Devuelve todos los miembros de la familia.
        """
        return self._members