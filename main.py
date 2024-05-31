import argparse
import math


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    square_root = int(math.sqrt(value)) + 1
    for i in range(2, square_root):
        if value % i == 0:
            return False
    return True


def prime_generator(start: int, end: int):
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        if is_prime(i):
            yield i


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, help="Start number")
    parser.add_argument("--end", type=int, help="End number")
    args = parser.parse_args()

    prime_numbers = list(prime_generator(args.start, args.end))
    print(prime_numbers)
