from suds.client import Client
from suds import WebFault

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

    def get_project(self,username):
        client = Client("http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
#        project = client.service.mc_enum(username) client.
        return project
