import mymath as mm
from Puasson import puasson
from Muavr_Laplas import muavr

def binom():
    with open("data.txt", "r") as f:
        for line in f.readlines():
            count_of_hit = 0
            lines = line.split(" ")
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    count_of_hit += mm.binF(i, p, n)
            print(f"{lines[0]} p = {p}, n = {n} prob = {count_of_hit}")


if __name__ == "__main__":
    print("Binomial distribution:")
    binom()
    print("Puasson formula:")
    puasson()
    print("Muavr-Laplas:")
    muavr()

