# Python Backend 

Progetti pratici di backend in Python.

## Progetti

### 1. User Registration & Auth API
API REST per la registrazione utenti scritta con FastAPI.
* **Stack:** `Python`, `FastAPI`, `Pydantic`, `pwdlib (Argon2id)`, `Uvicorn`
* **Cosa fa:** Valida i dati in ingresso con Pydantic, fa l'hashing delle password con Argon2id e usa Response Model dedicati per non restituire mai dati sensibili al client. Gestisce gli status code HTTP a seconda dei casi.

### 2. Server Log Analyzer & Reporter
Script per analizzare file di log di grandi dimensioni.
* **Stack:** `Python Standard Library` (`os`, `csv`, `json`, `collections`)
* **Cosa fa:** Legge i file riga per riga per non saturare la RAM, conta i livelli di errore con `collections` ed esporta il report finale in JSON e CSV.# python-backend-lab
Raccolta di progetti backend in Python: REST API con FastAPI, validazione Pydantic, sicurezza con Argon2id e script di log parsing.
