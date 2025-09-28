from multiprocessing import Pool
import random


def request_n():
    """Request a number of points from user."""
    n = int(input('Please, enter the total number of points you would like to use when estimating:\n'))
    while n % 10 != 0 or n < 1000:
        print('Your input is invalid. \nDue to computational reasons, the number of points should be '
              'more than 999 and should be multiple of 10.')
        n = int(input('Please, enter a new number, taking into account the rules above:\n'))
    return n


def count(n):
    """Count the number of points inside the quarter circle"""
    inside_count = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_count += 1
    return inside_count


def estimate():
    """Run parallel computing of Monte Carlo's π estimation."""
    CPU_cores = 10
    n = request_n()
    token = n // CPU_cores
    with Pool(CPU_cores) as p:
        inside = p.map(count, [token] * CPU_cores)
    total_inside = sum(inside)
    pi = 4 * total_inside / n
    return (pi, n)


if __name__ == "__main__":
    estimate()