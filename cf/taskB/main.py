def get_table(matrix):
    c = 0
    t = [{'TP': 0, 'FP': 0, 'FN': 0, 'cnt': 0} for _ in range(len(matrix))]
    for i in range(len(matrix)):
        t[i]['TP'] = matrix[i][i]
        for j in range(len(matrix)):
            t[i]['cnt'] += matrix[i][j]
            c += matrix[i][j]
            if j != i:
                t[i]['FP'] += matrix[j][i]
                t[i]['FN'] += matrix[i][j]
    return t, c


def get_micro_f_score(table, cnt):
    res = {'TP': 0, 'FP': 0, 'FN': 0}
    for c in table:
        res['TP'] += c['TP'] * c['cnt']
        res['FP'] += c['FP'] * c['cnt']
        res['FN'] += c['FN'] * c['cnt']
    precision = get_precision(res['TP'] / cnt, res['FP'] / cnt)
    recall = get_recall(res['TP'] / cnt, res['FN'] / cnt)
    return get_f_score(precision, recall)


def get_precision(tp, fp):
    if tp + fp == 0:
        return 0
    return tp / (tp + fp)


def get_recall(tp, fn):
    if tp + fn == 0:
        return 0
    return tp / (tp + fn)


def get_f_score(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * precision * recall / (precision + recall)


def get_macro_f_score(table, cnt):
    precision = 0
    recall = 0
    for p, r, c in table:
        precision += p * c
        recall += r * c
    return get_f_score(precision / cnt, recall / cnt)


def mean(table, cnt):
    s = 0
    for i in table:
        s += i
    return s / cnt


if __name__ == "__main__":
    k = int(input())
    confusion_matrix = [list(map(int, input().split())) for _ in range(k)]
    contingent_table, cnt = get_table(confusion_matrix)
    micro_f1_score = get_micro_f_score(contingent_table, cnt)
    precision_recall_table = [(get_precision(c['TP'], c['FP']), get_recall(c['TP'], c['FN']), c['cnt'])
                              for c in contingent_table]
    macro_f1_score = get_macro_f_score(precision_recall_table, cnt)
    f_score_table = [get_f_score(pre, rec) * c for pre, rec, c in precision_recall_table]
    f1_score = mean(f_score_table, cnt)
    print(micro_f1_score)
    print(macro_f1_score)
    print(f1_score)
