import argparse


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def prime_generator(start: int, end: int) -> list:
    if start > end:
        start, end = end, start
    prime_numbers = []
    for i in range(start, end):
        if is_prime(i):
            prime_numbers.append(i)

    return prime_numbers


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, help="Start number")
    parser.add_argument("--end", type=int, help="End number")
    args = parser.parse_args()

    prime_generator(args.start, args.end)
