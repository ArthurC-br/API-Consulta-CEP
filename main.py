import eel
import api

cepObj = api.CEP()

@eel.expose
def getCep(cep):
    msg = cepObj.getInfo(cep)
    eel.setmsg(msg['cep'], msg['uf'], msg['localidade'], msg['logradouro'], msg['bairro'], msg['ddd'])

@eel.expose
def descubraCep(uf, cidade, end):
    msg = cepObj.getCEP(uf, cidade, end)
    for index in msg:
        eel.setmsg(index['cep'], index['uf'], index['localidade'], index['logradouro'], index['bairro'], index['ddd'])


eel.init("www")
eel.start("index.html", size=(320, 460))



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

