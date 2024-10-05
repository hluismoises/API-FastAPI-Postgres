from pydantic import BaseModel
from datetime import date

class Movie(BaseModel):
    id: int
    autor: str
    description: str
    fecha_estreno: date
