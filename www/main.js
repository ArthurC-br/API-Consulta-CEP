function button(){
    var cep = document.getElementById("inputCep");
    eel.getCep(cep.value);
}

function descubra1Cep(){
    console.log("teste")
    var uf = document.getElementById("uf")
    var cidade = document.getElementById("city")
    var rua = document.getElementById("logradouro")

    eel.descubraCep(uf.value, cidade.value, rua.value)

}

eel.expose(setmsg)
function setmsg(cep, estado, cidade, rua, bairro, ddd){
    var h3 = document.getElementById("cep");
    h3.textContent = "CEP: " + cep
    var h3 = document.getElementById("estado");
    h3.textContent = "Estado: " + estado
    var h3 = document.getElementById("cidade");
    h3.textContent = "Cidade: " + cidade
    var h3 = document.getElementById("rua");
    h3.textContent = "Rua: " + rua
    var h3 = document.getElementById("bairro");
    h3.textContent = "Bairro: " + bairro
    var h3 = document.getElementById("ddd");
    h3.textContent = "DDD: " + ddd;
}

