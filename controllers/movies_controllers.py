from fastapi import APIRouter
from models import Movie
from database import conn

router = APIRouter()

@router.get("/movies")
def get_movies():
    temporal_array = []
    with conn.cursor() as cur:
        try:
            query = "SELECT * FROM my_movies"
            cur.execute(query)
            movies = cur.fetchall()
            for row in movies:
                temporal_array.append({"id": row[0], "autor": row[1], "description": row[2], "fecha_estreno": row[3]})
            return {"message": temporal_array}
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            return {"error": "Error al obtener las movies"}

@router.get("/movie/{movie_id}")
def get_movie_by_id(movie_id: int):
    with conn.cursor() as cur:
        try:
            query = "SELECT * FROM my_movies WHERE id = %s"
            cur.execute(query, (movie_id,))
            movie = cur.fetchone()
            if movie:
                return {
                    "id": movie[0],
                    "autor": movie[1],
                    "description": movie[2],
                    "fecha_estreno": movie[3]
                }
            else:
                return {"message": "Movie no encontrada"}
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            return {"error": "Error al obtener la movie"}

@router.post("/movie", status_code=201)
def create_movie(movie: Movie):
    with conn.cursor() as cur:
        try:
            query = "INSERT INTO my_movies (autor, description, fecha_estreno) VALUES (%s, %s, %s)"
            values = (movie.autor, movie.description, movie.fecha_estreno)
            cur.execute(query, values)
            conn.commit()
            return {"message": "Movie creada correctamente"}
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            return {"error": "Error al crear la movie"}

@router.put("/movie/{movie_id}")
def update_movie(movie_id: int, movie: Movie):
    with conn.cursor() as cur:
        try:
            query = "UPDATE my_movies SET autor = %s, description = %s, fecha_estreno = %s WHERE id = %s"
            values = (movie.autor, movie.description, movie.fecha_estreno, movie_id)
            cur.execute(query, values)
            conn.commit()
            return {"message": "Movie actualizada correctamente"}
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            return {"error": "Error al actualizar la movie"}

@router.delete("/movie/{movie_id}")
def delete_movie(movie_id: int):
    with conn.cursor() as cur:
        try:
            query = "DELETE FROM my_movies WHERE id = %s"
            values = (movie_id,)
            cur.execute(query, values)
            conn.commit()
            return {"message": "Movie eliminada correctamente"}
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {e}")
            return {"error": "Error al eliminar la movie"}
