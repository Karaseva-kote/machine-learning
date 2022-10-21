import numpy as np

if __name__ == "__main__":
    n = int(input())
    x1 = []
    x2 = []
    for i in range(n):
        a, b = map(int, input().split())
        x1.append(a)
        x2.append(b)
    x1 = np.array(x1)
    x2 = np.array(x2)
    order = x1.argsort()
    x1_ranks = order.argsort()
    order = x2.argsort()
    x2_ranks = order.argsort()
    print(np.corrcoef(x1_ranks, x2_ranks)[0][1])
