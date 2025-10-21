import mysql.connector
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_connection():
    """Cria e retorna uma conexão com o banco de dados MySQL"""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "camila_database")
    )
