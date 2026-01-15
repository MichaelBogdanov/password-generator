import argparse
from random import choice
from string import ascii_letters, digits

import pyperclip

SPECIAL_CHARS = '!@#$%^&*()_+=-{}[]|\\;:\'",.<>/?'


def generate_password(length: int) -> str:
    """Генерирует случайный пароль заданной длины."""
    allowed_chars = ascii_letters + digits + SPECIAL_CHARS
    return ''.join(choice(allowed_chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=8, help='Длина пароля')
    args = parser.parse_args()

    if args.length <= 0:
        print("Длина пароля должна быть положительным числом")
        return

    password = generate_password(args.length)
    print(password)
    pyperclip.copy(password)
    print("(Пароль скопирован в буфер обмена!)")


if __name__ == '__main__':
    main()
