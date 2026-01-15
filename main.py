import argparse
from random import choice
from string import ascii_letters, digits


parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, default=8, help='Длина пароля')
args = parser.parse_args()

alphabet = ascii_letters + digits + '!@#$%^&*()_+=-{}[]|\\;:\'",.<>/?'
for _ in range(args.length):
    print(choice(alphabet), end='', flush=True)

