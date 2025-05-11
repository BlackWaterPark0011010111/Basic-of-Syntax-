import random
import string

def generate_random_string(length=8, *args, **kwargs):
    symbols = ''.join(args) if args else string.ascii_letters + string.digits
    password = ''.join(random.choice(symbols) for i in range(length))
    if kwargs.get('uppercase', False):
        password = password.upper()
    if kwargs.get('special_chars', False):
        password = ''.join(random.choice(string.punctuation) for _ in range(2)) + password
    return password

# Example usage
password = generate_random_string(12, string.ascii_lowercase, string.digits, uppercase=True, special_chars=True)
print(password)
