import mymath as mm
import time
from Puasson import puasson
from Muavr_Laplas import muavr


def binom():
    with open("data.txt", "r") as f:
        mas_bin =[]
        for line in f.readlines():
            times = time.time()
            count_of_hit = 0
            lines = line.split(" ")
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    count_of_hit += mm.binF(i, p, n)
            times = time.time() - times
            print(f"{lines[0]} p = {p}, n = {n}, prob. = {count_of_hit}")
            print(f"Time to calculate: {times} sec\n")
            mas_bin.append(count_of_hit)
        return mas_bin


if __name__ == "__main__":
    print("Binomial distribution:\n")
    m_bin = binom()
    print("Puasson formula:\n")
    puasson(m_bin)
    print("Muavr-Laplas:\n")
    muavr(m_bin)

