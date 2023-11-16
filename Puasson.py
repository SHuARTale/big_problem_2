import mymath as mm
import time
from decimal import Decimal

def puasson(b_mas):
    with open("data.txt", "r") as f:
        for line in f.readlines():
            times = time.time()
            count_of_hit = 0
            lines = line.split(" ")
            numb = int(lines[0].replace(")",""))
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    m = mm.puassonF(i,p,n)
                    count_of_hit += m
            times = time.time() - times
            print(f"{lines[0]} p = {p}, n = {n}, prob. = {count_of_hit}.")
            print(f"Diffenent Bin/Puasson = {abs(Decimal(count_of_hit)-b_mas[numb-1])}")
            print(f"Time to calculate: {times} sec\n")
