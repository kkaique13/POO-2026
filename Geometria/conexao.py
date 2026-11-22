import os
import pymysql as MySQLdb
from dotenv import load_dotenv
from typing import cast

load_dotenv()

host = cast(str, os.getenv("DB_HOST"))
user = cast(str, os.getenv("DB_USER"))
password = cast(str, os.getenv("DB_PASSWORD"))
database = cast(str, os.getenv("DB_NAME"))

if not all([host, user, password, database]):
    raise ValueError("Configurações do .env incompletas.")

assert host is not None and user is not None and password is not None and database is not None

def conectar():
    return MySQLdb.connect(host=host, user=user, password=password, database=database)