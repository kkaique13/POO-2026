#Importando a biblioteca para conectar o python com o banco de dados
import pymysql as MySQLdb
import os
from dotenv import load_dotenv
from typing import cast

#Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

#Recuperando as informações para conectar ao banco de dados
host = cast(str, os.getenv("DB_HOST"))
user = cast(str, os.getenv("DB_USER"))
password = cast(str, os.getenv("DB_PASSWORD"))
database = cast(str, os.getenv("DB_NAME"))

#Verificando se todas as informações foram carregadas corretamente
assert host is not None and user is not None and password is not None and database is not None

#Função para conectar o python com o banco de dados
def conectar():
    return MySQLdb.connect(host=host,user=user,password=password,database=database)