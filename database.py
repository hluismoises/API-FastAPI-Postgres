import psycopg2

db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'db',
    'port': '5432'
}

conn = psycopg2.connect(**db_params)

# Función para crear la tabla my_movies e insertar datos
def init_db():
    cursor = conn.cursor()

    # Consulta para crear la tabla si no existe
    query = """
        CREATE TABLE IF NOT EXISTS my_movies (
            id SERIAL PRIMARY KEY,
            autor VARCHAR(100),
            description VARCHAR(100),
            fecha_estreno DATE
        )
    """
    cursor.execute(query)
    conn.commit()

    insert_query = '''
    INSERT INTO my_movies (autor, description, fecha_estreno) VALUES (%s, %s, %s)
    '''
    # Datos a insertar
    data_to_insert = [
        ('Christopher Nolan', 'A mind-bending thriller', '2010-07-16'),
        ('Quentin Tarantino', 'A classic crime film', '1994-10-14'),
        ('Steven Spielberg', 'An epic science fiction adventure', '1993-06-11')
    ]

    cursor.executemany(insert_query, data_to_insert)
    conn.commit()
    
  


