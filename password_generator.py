import secrets
import string

def genera_password(lunghezza: int = 16, speciali: bool = True)->str:
    if lunghezza < 8:
        raise ValueError('La lunghezza minima consigliata è di almeno 8 caratteri.')
    lettere_minuscole = string.ascii_lowercase
    lettere_maiuscole = string.ascii_uppercase
    cifre = string.digits
    simboli = "!@#$%^&*()-_=+[]{}<>?" if speciali else ''
    
    pool = lettere_maiuscole + lettere_minuscole + cifre + simboli  
    password = [
        secrets.choice(lettere_minuscole),
        secrets.choice(lettere_maiuscole),
        secrets.choice(cifre),
    ]
    if speciali :
        password.append(secrets.choice(simboli))
    password +=[secrets.choice(pool) for _ in range (lunghezza - len(password))]
    secrets.SystemRandom().shuffle(password)
    return''.join(password)

if __name__ == "__main__":
    print("--- Test Generatore Password ---")
    
    pw_default = genera_password()
    print(f"Password standard (16 char): {pw_default}")

    pw_senza_simboli = genera_password(lunghezza=20, speciali=False)
    print(f"Password alfanumerica (20 char): {pw_senza_simboli}")

    print("\nBatch di 5 password (12 char):")
    for i in range(1, 6):
        print(f"{i}. {genera_password(lunghezza=12)}")