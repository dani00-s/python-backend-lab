import re
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, model_validator

app = FastAPI(title="Registrazione Utenti - Validazione Avanzata")

# Corretto il tipo delle chiavi: int invece di str
fake_users_db: dict[int, dict] = {}

class UserRegisterIn(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="solo caratteri alfanumerici o underscore",  # Aggiunta virgola
    )
    email: EmailStr  # In minuscolo e indentato nella classe
    eta: int = Field(..., ge=18, le=120, description="L'utente deve avere almeno 18 anni")
    password: str = Field(..., min_length=8, description="Minimo 8 caratteri")
    conferma_password: str = Field(..., description="Deve coincidere con la password")

    @model_validator(mode="after")
    def verifica_conferma_password(self):
        if self.password != self.conferma_password:
            raise ValueError("Le password inserite non coincidono")
        return self

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    eta: int

@app.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Registra un nuovo utente",  # Aggiunta virgola sopra
)
def register(user_data: UserRegisterIn):
    for existing_users in fake_users_db.values():
        if existing_users["email"] == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email già registrata",
            )
        if existing_users["username"] == user_data.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username già in uso",
            )

    new_id = len(fake_users_db) + 1

    fake_users_db[new_id] = {
        "id": new_id,
        "username": user_data.username,
        "email": user_data.email,
        "eta": user_data.eta,
        "hashed_password": f"hash_finto_{user_data.password}",
    }
    return fake_users_db[new_id]
