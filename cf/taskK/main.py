import numpy as np

if __name__ == "__main__":
    n = int(input())
    x1 = []
    x2 = []
    for i in range(n):
        a, b = map(int, input().split())
        x1.append(a)
        x2.append(b)
    print(np.corrcoef(x1, x2)[0][1])

