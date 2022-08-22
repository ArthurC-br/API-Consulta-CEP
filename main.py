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


