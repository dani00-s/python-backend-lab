import secrets

def generate_api_key(prefix: str = 'sk_live',nybytes: int = 32) -> str:
    random_part = secrets.token_urlsafe(nybytes)
    clean_prefix = prefix.rstrip('_')
    return f'{clean_prefix}_{random_part}'

if __name__ == '__main__':
    live_key = generate_api_key('sk_live')
    print(f'API Key Live: {live_key}')

    test_key = generate_api_key('sk_test')
    print(f"API Key Test: {test_key}")

    short_key = generate_api_key('pk_live',nybytes=16)
    print(f"API Key Pubblica: {short_key}")
