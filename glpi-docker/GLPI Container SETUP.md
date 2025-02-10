
Referencias :
<br>
-----------------------------------------------------------------------------
<br>
https://github.com/glpi-project/glpi
https://github.com/fusioninventory/fusioninventory-for-glpi/
<br>
<h2>Setup GLPI Container :</h2>
<br>
Instale o Diretório oficial do GLPI from: https://github.com/glpi-project/glpi

<br>
<h2>Insira estes dois arquivos docker no diretório oficial do GLPI</h2> 
<br>
- Dockerfile
<br>
- docker-compose.yml
<br>
<br>
<h4>Será necessário dar permissão para dois diretórios presentes no diretório oficial <b>glpi/</b> :</h4>
<br>
- Files
<br>
- Config
<br>
<br>

```
sudo chmod +777 /home/estagiario/projects/glpi/config/
sudo chmod +777 /home/estagiario/projects/glpi/files/
---------------------------------------------------------
sudo chown -U 33:33 /home/estagiario/projects/glpi/config/
sudo chown -U 33:33 /home/estagiario/projects/glpi/files/
```

--------------------------------------------------------

<h2>Inicie o docker-compose</h2>
<br>
```
docker compose up --build -d
```
<br>
Verifique se os dois arquivos estão sendo executados corretamente.