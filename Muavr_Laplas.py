import mymath as mm
import math
import time
from scipy.integrate import quad
from scipy import inf
from decimal import Decimal


def local(b_mas):
    with open("data.txt", "r") as f:
        for line in f.readlines():
            times = time.time()
            count_of_hit = 0
            lines = line.split(" ")
            numb = int(lines[0].replace(")", ""))
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    m = mm.Muav_Lapl(i, p, n)
                    count_of_hit += m
            times = time.time() - times
            print(f"{lines[0]} p = {p}, n = {n} prob = {count_of_hit}.")
            print(f"Diffenent Bin/Muavr-Laplas(local) = {abs(Decimal(count_of_hit)-b_mas[numb-1])}")
            print(f"Time to calculate: {times} sec\n")

def integrand(t):
    return 1 / (math.sqrt(2 * math.pi)) * pow(math.e, -(pow(t, 2) / 2))


def integral(b_mas):
    with (open("data.txt", "r") as f):
        for line in f.readlines():
            times = time.time()
            count_of_hit: float = 0.0
            lines = line.split(" ")
            numb = int(lines[0].replace(")", ""))
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                sig = math.sqrt(n * p * (1 - p))
                u = n * p
                if n * p - 1 <= i <= n * p + 1:
                    a = quad(integrand, -inf, ((n * p - 1) - u) / sig)
                    b = quad(integrand, -inf, ((n * p + 1) - u) / sig)
                    count_of_hit += (b[0] - a[0])/2
            times = time.time() - times
            print(f"{lines[0]} p = {p}, n = {n}, prob. = {count_of_hit}.")
            print(f"Diffenent Bin/Muavr-Laplas(integral) = {abs(Decimal(count_of_hit)-b_mas[numb-1])}")
            print(f"Time to calculate: {times} sec\n")


def muavr(mas):
    print("Local variant:")
    local(mas)
    print("Integral variant:")
    integral(mas)
