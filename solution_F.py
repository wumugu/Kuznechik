def collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def main():
    seq = collatz(17)          # 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
    pos = 0
    seen = {pos}
    jump = 0
    while True:
        # верхний листочек стопки, после прыжка он уходит вниз, поэтому стопка циклическая
        step = seq[jump % len(seq)]
        jump += 1
        # нечётный по номеру прыжок вправо, чётный влево
        pos += step if jump % 2 == 1 else -step
        if pos in seen:
            print(pos)
            return
        seen.add(pos)


if __name__ == "__main__":
    main()
