import sys


def round_massive(n, m):
    i = 1
    res = []
    while True:
        res += str(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return res


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    res = ''.join(round_massive(n, m))
    print(res, end='\n')