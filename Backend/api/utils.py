import random


def generate_code():
    digits = [str(random.randint(0, 9)) for _ in range(5)]
    return ''.join(digits)
