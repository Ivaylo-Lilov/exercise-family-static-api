
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []
        self._next_id = 1 

    def _generateId(self):
        return self._next_id

    def add_member(self, member):
        
        if "id" not in member:
            member["id"] = self._generateId()
            self._next_id += 1
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members