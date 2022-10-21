import numpy as np


def grad(x, y, pred):
    den = abs(pred) + abs(y)
    if den == 0:
        return [0 for _ in x]
    multiplier = np.sign(pred - y) / den - np.sign(pred) * abs(pred - y) / den ** 2
    return [x_i * multiplier for x_i in x]


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [list(map(float, input().split())) for _ in range(n)]
    x = [line[:-1] + [1.0] for line in data]
    y = [line[-1] for line in data]
    a = list(map(int, input().split()))
    for x_i, y_i in zip(x, y):
        print(*(grad(x_i, y_i, np.dot(a, x_i))))