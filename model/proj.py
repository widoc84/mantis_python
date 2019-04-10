from sys import maxsize

class Proj:

    def __init__(self,id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and self.description == other.description

    def id_or_nmx(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize