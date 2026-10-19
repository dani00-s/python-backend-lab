from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

# Inizializzazione del motore di hashing Argon2id
pwd_context = PasswordHash((Argon2Hasher(),))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


if __name__ == "__main__":
    segreto = input("Scrivi la password da registrare: ")
    hash_generato = hash_password(segreto)
    print("Hash generato:", hash_generato)
    test_input = input("Riscrivi la password per verificare: ")
    print("Test password corretta:", verify_password(test_input, hash_generato))
    print("Test password errata:", verify_password("Sbagliata!", hash_generato))
