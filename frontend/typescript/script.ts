function exibeListaDeParticipantes() {
    fetch(backendAddress + "participantes/lista/")
        .then(response => response.json())
        .then(participantes => {
            let campos = ['id', 'nome', 'sobrenome', 'distancia', 'tempo'];
            let tbody = document.getElementById('idtbody') as HTMLTableSectionElement;
            tbody.innerHTML = "";

            /* novo */
            const searchInput = (document.getElementById('searchInput') as HTMLInputElement)?.value.toLowerCase();

            for (let participante of participantes) {
                let tr = document.createElement('tr') as HTMLTableRowElement;

                /* novo */
                if (!searchInput) {
                    for (let i = 0; i < campos.length; i++) {
                        let td = document.createElement('td') as HTMLTableCellElement;
                        let href = document.createElement('a') as HTMLAnchorElement;
                        href.setAttribute('href', 'update.html?id=' + participante['id']);
                        let texto = document.createTextNode(participante[campos[i]]) as Text;
                        href.appendChild(texto);
                        td.appendChild(href);
                        tr.appendChild(td);
                    }
                } else {
                    let participanteEncontrado = participantes.find(p =>
                        campos.some(campo => p[campo].toString().toLowerCase().includes(searchInput))
                    );

                    if (participanteEncontrado) {
                        for (let i = 0; i < campos.length; i++) {
                            let td = document.createElement('td') as HTMLTableCellElement;
                            let href = document.createElement('a') as HTMLAnchorElement;
                            href.setAttribute('href', 'update.html?id=' + participanteEncontrado['id']);
                            let texto = document.createTextNode(participanteEncontrado[campos[i]]) as Text;
                            href.appendChild(texto);
                            td.appendChild(href);
                            tr.appendChild(td);
                        }
                    } else {
                        console.log("Aucun coureur n'a été trouvé");
                    }
                }

                let checkbox = document.createElement('input') as HTMLInputElement;
                checkbox.setAttribute('type', 'checkbox');
                checkbox.setAttribute('name', 'id');
                checkbox.setAttribute('id', 'id');
                checkbox.setAttribute('value', participante['id']);
                let td = document.createElement('td') as HTMLTableCellElement;
                td.appendChild(checkbox);
                tr.appendChild(td);
                tbody.appendChild(tr);
            }
        })
        .catch(error => {
            console.error("Erro:", error);
        });
}
