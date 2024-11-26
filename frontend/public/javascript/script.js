"use strict";
onload = function () {
    exibeListaDeParticipantes(); // exibe lista de participantes ao carregar a página
    document.getElementById('insere').addEventListener('click', evento => { location.href = 'insereParticipante.html'; });
    document.getElementById('remove').addEventListener('click', apagaParticipantes);
};
function exibeListaDeParticipantes() {
    fetch(backendAddress + "participantes/lista/")
        .then(response => response.json())
        .then(participantes => {
        let campos = ['id', 'nome', 'sobrenome', 'distancia', 'tempo'];
        let tbody = document.getElementById('idtbody');
        tbody.innerHTML = "";
        for (let participante of participantes) {
            let tr = document.createElement('tr');
            for (let i = 0; i < campos.length; i++) {
                let td = document.createElement('td');
                let href = document.createElement('a');
                href.setAttribute('href', 'update.html?id=' + participante['id']);
                let texto = document.createTextNode(participante[campos[i]]);
                href.appendChild(texto);
                td.appendChild(href);
                tr.appendChild(td);
            }
            let checkbox = document.createElement('input');
            checkbox.setAttribute('type', 'checkbox');
            checkbox.setAttribute('name', 'id');
            checkbox.setAttribute('id', 'id');
            checkbox.setAttribute('value', participante['id']);
            let td = document.createElement('td');
            td.appendChild(checkbox);
            tr.appendChild(td);
            tbody.appendChild(tr);
        }
    })
        .catch(error => {
        console.error("Erro:", error);
    });
}
let apagaParticipantes = (evento) => {
    evento.preventDefault();
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const checkedValues = [];
    checkboxes.forEach(checkbox => { checkedValues.push(checkbox.value); });
    fetch(backendAddress + "participantes/lista/", {
        method: 'DELETE',
        body: JSON.stringify(checkedValues),
        headers: { 'Content-Type': 'application/json', }
    })
        .then(response => {
        if (response.ok) {
            alert('Dados removidos com sucesso');
        }
        else {
            alert('Dados removidos com erro');
        }
    })
        .catch(error => { console.log(error); })
        .finally(() => { exibeListaDeParticipantes(); });
};
