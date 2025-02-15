## Installation  
<br>
1 - Instale o fusioninventory-agent :
<br>
<br>

```
╭─ 💁 estagiario at 💻 estagiario in 📁 ~/GLPI-NETBOX-Integration on (🌿 main ✓)
╰λ sudo apt install fusioninventory-agent
```
<br>
2 - Instale o agent específico para a coleta no VCenter presente em :
<br>
https://documentation.fusioninventory.org/FusionInventory_agent/installation/linux/deb/ 
<br>
<br>
💻 Existem documentações para as outras Distribuições Linux e para Windows !!
<br>
<br>
O arquivo a ser baixado -> fusioninventory-agent-task-esx_2.5.2-1_all.deb
<br>
<br>

```
╭─ 💁 estagiario at 💻 estagiario in 📁 ~/Downloads
╰λ dpkg -i fusioninventory-agent-task-esx_2.5.2-1_all.deb 
```


## Usage 
<br>
3 - No GLPI será necessária a configuração de alguns paramêtros para a coleta no VCenter.
<br>
<br>
Crie um novo 'Remote devices to inventory' e para este remote device crie um 'Authentication for remote devices', credencias de vizualização apenas no VCenter.








<br>
<br>
<br>
4 - Rode o fusioninventory-agent depois que o plugin já esteja estabelecido no GLPI:
<br>
<br>

```
╭─integration 💁 estagiario at 💻 estagiario in 📁 ~
╰λ sudo fusioninventory-agent
```
<br>

```
╰λ sudo fusioninventory-agent
[info] target server0: server http://localhost:8080/
[info] sending prolog request to server0
[info] running task ESX
[error] [http client] Can't decode JSON content, starting with 
[info] No job schedule returned from server at http://localhost:8080/
[info] running task Collect
[error] [http client] Can't decode JSON content, starting with 
[info] No job schedule returned from server at http://localhost:8080/
[info] running task Inventory
[info] New inventory from ilak-2025-02-05-09-42-02 for server0
[info] 'scan-homedirs' configuration parameters disabled, ignoring virtualbox virtual machines in user directories
```
<br>
- A info 'No job schedule returned from server at http://localhost:8080/' 
<br>
Indica que na aplicação do GLPI as configurações de uma task ainda não foram efetuadas, sendo necessárias para o funcionamento do plugin