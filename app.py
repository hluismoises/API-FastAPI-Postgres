from fastapi import FastAPI
from database import init_db
from controllers.movies_controllers import router as movies_router

app = FastAPI()

# Evento que se ejecuta al inicio de la aplicación
@app.on_event("startup")
def on_startup():
    # Llama a la función que crea la tabla
    init_db()

app.include_router(movies_router)
