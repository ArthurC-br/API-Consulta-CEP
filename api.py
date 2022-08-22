import requests

class CEP:
    def __init__(self):
        pass

    def validateCep(self, cep):
        if len(cep) == 8:
            if str(cep).isnumeric():
                return True
            else:
                return False
        else:
            return False

    def getInfo(self, cep):
        if self.validateCep(cep):
            self.url = f"http://viacep.com.br/ws/{cep}/json/"
            req = requests.request("get", self.url)
            return req.json()

        else:
            return "ERRO"


    def getCEP(self, uf, cidade, rua):

        self.url = f"http://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/"
        req = requests.request("get", self.url)
        return req.json()

