from math import *


def non_param_regh(x, train_x, train_y, k, ro, h):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(train_x)):
        d = ro(train_x[i], x)
        k_val = 0
        h_val = h([ro(x1, x) for x1 in train_x])
        if h_val == 0:
            if d == 0:
                k_val = k(0)
        else:
            k_val = k(d / h_val)
        sum1 += train_y[i] * k_val
        sum2 += k_val
    if sum2 == 0:
        return sum(y_train) / len(y_train)
    return sum1 / sum2


def get_dist(name):
    if name == 'manhattan':
        return lambda x1, x2: sum(abs(x1_i - x2_i) for x1_i, x2_i in zip(x1, x2))
    if name == 'euclidean':
        return lambda x1, x2: sqrt(sum((x1_i - x2_i) ** 2 for x1_i, x2_i in zip(x1, x2)))
    if name == 'chebyshev':
        return lambda x1, x2: max(abs(x1_i - x2_i) for x1_i, x2_i in zip(x1, x2))


check_absolute_1 = lambda x, val: 0 if abs(x) >= 1 else val


def get_kernel(name):
    if name == 'uniform':
        return lambda x: check_absolute_1(x, 1 / 2)
    if name == 'triangular':
        return lambda x: check_absolute_1(x, 1 - abs(x))
    if name == 'epanechnikov':
        return lambda x: check_absolute_1(x, 3 / 4 * (1 - x ** 2))
    if name == 'quartic':
        return lambda x: check_absolute_1(x, 15 / 16 * (1 - x ** 2) ** 2)
    if name == 'triweight':
        return lambda x: check_absolute_1(x, 35 / 32 * (1 - x ** 2) ** 3)
    if name == 'tricube':
        return lambda x: check_absolute_1(x, 70 / 81 * (1 - abs(x) ** 3) ** 3)
    if name == 'gaussian':
        return lambda x: 1 / (sqrt(2 * pi)) * e ** (-1 / 2 * x ** 2)
    if name == 'cosine':
        return lambda x: check_absolute_1(x, pi / 4 * cos(pi / 2 * x))
    if name == 'logistic':
        return lambda x: 1 / (e ** x + 2 + e ** (-x))
    if name == 'sigmoid':
        return lambda x: 2 / pi / (e ** x + e ** (-x))


def get_window(name, param):
    if name == 'fixed':
        return lambda x: param
    if name == 'variable':
        return lambda x: 0 if len(x) < param else sorted(x)[param]


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    X_train = [line[:-1] for line in data]
    y_train = [line[-1] for line in data]
    X_test = list(map(int, input().split()))
    dist = input()
    kernel = input()
    window_type = input()
    window = int(input())

    print(non_param_regh(X_test, X_train, y_train, get_kernel(kernel), get_dist(dist), get_window(window_type, window)))