import sys


def is_point_in_circle(filepath_one, filepath_two):

    with open(filepath_one, 'r') as file:
        xc, yc = map(float, file.readline().split())
        r = float(file.readline())

    with open(filepath_two, 'r') as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            x = float(line[0])
            y = float(line[1])
            if (x-xc) ** 2 + (y-yc) ** 2 <= r ** 2:
                if (x - xc) ** 2 + (y - yc) ** 2 == r ** 2:
                    print(0, end='\n')
                else:
                    print(1, end='\n')
            else:
                print(2, end='\n')


if __name__ == '__main__':
    is_point_in_circle(sys.argv[1], sys.argv[2])
