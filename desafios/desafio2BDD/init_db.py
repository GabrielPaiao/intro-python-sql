import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="joaol",
        password="aluno123",
        database="ifspjcrbdd"
    )