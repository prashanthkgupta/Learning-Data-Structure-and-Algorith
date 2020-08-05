def toh(x, z, y, n):
    if n == 1:
        print('move disk %d from %s -> %s ' % (n, x, z))
    else:
        toh(x, y, z, n - 1)
        print('move disk %d from %s -> %s ' % (n, x, z))
        toh(y, z, x, n - 1)


def toh_book():
    pass


def toh_it():
    pass


if __name__ == '__main__':
    toh('x', 'z', 'y', 3)
