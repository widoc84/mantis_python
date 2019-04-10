from suds.client import Client
from suds import WebFault
from model.proj import Proj

class SoapH:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project(self):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        test = client.service.mc_projects_get_user_accessible('administrator','root')
        list = []
        for i in test:
            id = i.id
            name = i.name
            description = i.description
            tmp_list = Proj(id=id, name=name, description=description)
            list.append(tmp_list)
        return list

    def add(self,proj):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
