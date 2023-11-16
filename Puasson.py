import mymath as mm


def puasson():
    with open("data.txt", "r") as f:
        for line in f.readlines():
            count_of_hit = 0
            lines = line.split(" ")
            p = float(lines[1])
            n = int(lines[2])
            for i in range(1, n + 1):
                if n * p - 1 <= i <= n * p + 1:
                    m = mm.puassonF(i,p,n)
                    count_of_hit += m
            print(f"{lines[0]} p = {p}, n = {n} prob = {count_of_hit}")

