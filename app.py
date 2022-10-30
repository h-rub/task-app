import sqlite3

try:
    connection = sqlite3.connect("/Users/heverrubio/task-app/loop-task.db")
    print("Conexión exitosa")
except:
    print("Ocurrió un error")

cursor = connection.cursor()

def insertar_datos(name, last_name, job_title, email, password):
    query = """INSERT INTO usuarios (name, last_name, job_title, email, password)
    VALUES (?, ?, ?, ?, ?)"""
    try:
        cursor.execute(query, (name, last_name, job_title, email, password))
        connection.commit()
        print("Se creó el objeto correctamente")
    except:
        print("Ocurrió un error al ejecutar la consulta")

def listar_dato_por_pk(pk):
    query_consulta = "SELECT * FROM usuarios WHERE pk = ?"
    response = cursor.execute(query_consulta, (pk, ))

    return response.fetchall()

def listar_todos_los_datos():
    query_consulta = "SELECT * FROM usuarios"
    response = cursor.execute(query_consulta)

    return response.fetchall()

if __name__ == "__main__":
    #insertar_datos(name = "Pepe", last_name = "Toño", job_title = "CPO", email = "pepe@gmail.com", password = "123456")
    lista_usuarios = listar_todos_los_datos()
    
    for usuarios in lista_usuarios:
        print(usuarios)