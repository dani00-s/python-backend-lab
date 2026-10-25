import secrets

def generate_api_key(prefix: str = 'sk_live',  nybytes: int = 10) -> str:
    random_part = secrets.token_urlsafe(nybytes)
    clean_prefix = prefix.rstrip('_')
    return f'{clean_prefix}_{random_part}'

if __name__ == '__main__':
    live_key = generate_api_key('')
    print(f'API Key Live: {live_key}')

    test_key = generate_api_key('')
    print(f"API Key Test: {test_key}")

    short_key = generate_api_key('',nybytes=10)
    print(f"API Key Pubblica: {short_key}")
