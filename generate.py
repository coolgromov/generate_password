import random
import string

def generate_password(length, use_digits, use_special_chars):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Длина пароля: "))
use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
use_special_chars = input("Использовать спецсимволы? (y/n): ").lower() == 'y'
password = generate_password(length, use_digits, use_special_chars)
print(f"Ваш пароль: {password}")
