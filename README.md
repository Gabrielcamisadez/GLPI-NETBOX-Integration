# GLPI-NETBOX-Integration
trainee project !!

<h2>VMware integration with Netbox</h2>

Este projeto visa uma automatização no processo de atualização de informações no Netbox, a partir de informações atualizadas do VCenter - VMware.
<br>
<br>
Nativamente o Netbox ainda não possui um plugin específico para esta tarefa, sendo assim o GLPI tem a capacidade de realizar um papel essencial neste processo, pois com o plugin 'Fusioninventory' temos a possibilidade de coletar dados do VCenter - VMware, e então transmitir estes dados para o Netbox.
<br>
<br>
O GLPI e o Netbox possuem sua própria RestAPI, no qual utilizarei para realizar a transmissão dos dados do GLPI para o Netbox.
<br>
Utilizarei o python para este funcionamento.


<h4>Tecnologias utilizadas :</h4>
- Python
<br>

<h4>Ferramentas utilizadas :</h4>
- Netbox
- GLPI
- VMware - VCenter