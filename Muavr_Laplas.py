import mymath as mm
import math
from scipy.integrate import quad
from scipy import inf


def local():
    with open("data.txt", "r") as f:
        for line in f.readlines():
            count_of_hit = 0
            lines = line.split(" ")
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    m = mm.Muav_Lapl(i, p, n)
                    count_of_hit += m
            print(f"{lines[0]} p = {p}, n = {n} prob = {count_of_hit}")


def integrand(t):
    return 1 / (math.sqrt(2 * math.pi)) * pow(math.e, -(pow(t, 2) / 2))


def integral():
    with (open("data.txt", "r") as f):
        for line in f.readlines():
            count_of_hit: float = 0.0
            lines = line.split(" ")
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                sig = math.sqrt(n * p * (1 - p))
                u = n * p
                if n * p - 1 <= i <= n * p + 1:
                    a = quad(integrand, -inf, ((n * p - 1) - u) / sig)
                    b = quad(integrand, -inf, ((n * p + 1) - u) / sig)
                    count_of_hit += (b[0] - a[0])/2
            print(f"{lines[0]} p = {p}, n = {n} prob = {count_of_hit}")


def muavr():
    print("Local variant:")
    local()
    print("Integral variant:")
    integral()

