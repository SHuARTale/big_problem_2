import math
from decimal import Decimal


def fack(n: int):
    res = 1
    if n <= 1: return res
    for i in range(2, n + 1):
        res *= i
    return res


def numbOfComb(k, N):
    return Decimal(fack(N)) / (Decimal(fack(k)) * Decimal(fack(N - k)))


def binF(k, p, N):
    return numbOfComb(k, N) * Decimal(pow(p, k)) * Decimal(pow((1 - p), N - k))


def puassonF(m, p, n):
    return (Decimal(pow(n * p, m)) / Decimal(fack(m))) * Decimal(pow(math.e, -(n * p)))


def Muav_Lapl(m,p,n):
    u = n*p
    sig = math.sqrt(n*p*(1-p))
    return (1/sig)*1/(math.sqrt(2*math.pi))*pow(math.e,-pow(((m-u)/sig),2)/2)
