from typing import List, Optional
import httpx
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel,Field


app = FastAPI(title="Gestione libri API")

class BookResult(BaseModel):
    title: str
    authors: List[str]
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    cover_url: Optional[str] = None

class BookCreate(BaseModel):
    titolo: str = Field(...,min_length=1,example="Il nome della rosa")
    autore: str = Field(...,min_length=1,example="Umberto Eco")
    pagine: int=Field(...,gt=0,example=500)
    genre:Optional[str] = Field(default=None,example="giallo storico")

books_db=[
        {"id": 1, "titolo": "Il nome della rosa", "autore": "Umberto Eco", "pagine": 500, "genere": "Giallo storico"},
        {"id": 2, "titolo": "Dune", "autore": "Frank Herbert", "pagine": 688, "genere": "Fantascienza"},
        {"id": 3, "titolo": "Fondazione", "autore": "Isaac Asimov", "pagine": 255, "genere": "Fantascienza"},
    ]
current_id = 3


@app.get("/books",status_code=status.HTTP_200_OK)
def get_books(genere:Optional[str] = None):
    if genere:
        risultati = [b for b in books_db if b.get('genere') and b['genere'].lower() == genere.lower()]
        return risultati
    return books_db

@app.get('/books/{book_id}',status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    for book in books_db:
        if book ["id"] ==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"libro con ID{book_id} non trovato"
    )

@app.get("/search-openlibrary", response_model=List[BookResult])
async def search_openlibrary(q: str = Query(..., description="Cerca su Open Library")):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://openlibrary.org/search.json",
            params={"q": q},
            headers={"User-Agent": "BookFinder/1.0"},
        )
        r.raise_for_status()
        return [BookResult(
            title=d.get("title", "Sconosciuto"),
            authors=d.get("author_name", ["Sconosciuto"]),
            publisher=d.get("publisher", [None])[0],
            published_date=str(d.get("first_publish_year", "")) or None,
            cover_url=f"https://openlibrary.org{d.get('cover_i')}-L.jpg" if d.get("cover_i") else None
        ) for d in r.json().get("docs", [])[:15]]

@app.post("/books",status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    global current_id
    current_id += 1

    new_book = book_data.model_dump()
    new_book['id'] = current_id

    books_db.append(new_book)
    return new_book

@app.delete('/books/{book_id}',status_code=status.HTTP_200_OK)
def delete_book(book_id:int):
    for index,book in enumerate(books_db):
        if book['id']==book_id:
            removed_book = books_db.pop(index)
        return{"message": "Libro rimosso con successo", "libro": removed_book}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'libro con id {book_id} non trovato '
    )
        
    
    
