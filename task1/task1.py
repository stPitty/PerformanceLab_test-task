def round_massive(n, m):
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break


if __name__ == '__main__':
    n, m = map(int, input().split())
    round_massive(n, m)
