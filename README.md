# GeoJSON MongoDB
Atividade prática da disciplina de Banco de Dados NOSQL

### Pre requisitos
1. Python
2. MongoDB

### Informações gerais
A proposta dessa atividade é aplicar o conhecimento adquirido em sala de aula sobre GeoJSON no MongoDB. O objetivo da atividade era: 

   - **Item 1**: Converter as coordenadas dos restaurantes da base de dados presente no arquivo [primer-dataset.json](https://github.com/mrayanealves/geojson-mongo/blob/master/primer-dataset.json) no padrão GeoJSON;
   
   - **Item 2**: Criar um index *2dsphere* para o novo campo criado; e
   
   - **Item 3**: Listar todos os restaurantes que estiverem até 1km de distância do Port Authority Bus Terminal (NY) (Coordenadas: -73.9929943, 40.7571707).
   
### Como executar
Para executar o projeto, primeiramente clone esse repositório em sua máquina e certifique-se de que o MongoDB esteja executando na porta padrão (27017).

#### Importando a base de dados
A base de dados que estamos trabalhando está nesse repositório no arquivo [primer-dataset.json](https://github.com/mrayanealves/geojson-mongo/blob/master/primer-dataset.json) (já citado anteriormente). 

Você pode importar esses dados através de alguma interface de sua preferência, ou por linha de comando mesmo. Nesse segundo caso, se você não souber como fazer, siga o [tutorial](https://docs.mongodb.com/guides/server/import/) do manual do MongoDB, ou [esse tutorial](https://petrim.com.br/blog/index.php/2018/08/22/mongoimport-importando-arquivos-json/) da internet que eu achei bem objetivo. 

Aqui na minha máquina, eu uso o docker com um container MongoDB. Para importar esses dados, eu sigo os seguintes passos:

1. Primeiramente, ao subir o container do mongo no docker eu mapeio uma pasta na minha máquina que funciona como a pasta /data do mongo, seguido o seguinte comando: 

~~~
$ sudo docker run -p 27017:27017 --name nosql-mongo -v /home/mongo:/data -d mongo
~~~

2. Em seguida, eu coloco o arquivo *primer-dataset.json* na minha pasta /home/mongo

3. Depois, eu acesso o conteiner do mongo com permissões de root (na pasta /bin/bash):

~~~
$ docker exec -it nosql-mongo /bin/bash
~~~

4. E, por fim, eu executo o comando 

~~~
$ mongoimport --db geojson --collection restaurants --drop --file /data/primer-dataset.json 
~~~

É importante sugerir que o nome do seu banco de dados deve ser **geojson** e sua coleção deve se chamar **restaurants**, para ficar consistente com o código e não ser necessária nenhuma mudança. Caso você não queira, altere as linhas 9 e 10 para `db = mongo_client.<nome da sua base de dados; ex: test, geojson>` e `collection = db.<nome da sua coleção; exemplo: restaurants>`, respectivamente.

#### Executando a solução
Com a base de dados devidamente importada, importe o *pymongo* com o comando ```pip3 install pymongo``` e rode execute o arquivo *main.py* com o python3 (```python3 main.py```). 

O que vai ser retornado para você, no final, é o resultado da consulta do **Item 3** descrito no tópico anterior. Para ver a mudança aos poucos, você pode printar o valor da primeira busca antes da modificação das coordenadas, printar depois de modificado (**Item 2**) e, por fim, printar o resultado da consulta no **Item 3**. 

Pronto! Fique a vontade para mudar o que quiser.
