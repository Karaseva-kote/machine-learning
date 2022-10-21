def uniform_split(data, m, k):
    data = list(data)
    parts = [[] for _ in range(k)]
    for i in range(0, len(data)):
        data[i] = (data[i], i + 1)
    data = sorted(data)
    ind = 0
    for c, i in data:
        parts[ind % k].append(i)
        ind += 1
    return parts


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    parts = uniform_split(data, m, k)
    for part in parts:
        print(len(part), *(el for el in sorted(part)))
