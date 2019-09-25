def solution(A, B):
    disjoint_intervals = []
    intervals = list(zip(A, B))
    intervals.sort(key=lambda x: x[0])

    for interval in intervals:
        if not disjoint_intervals:
            disjoint_intervals.append(interval)
        else:
            last = disjoint_intervals[-1]
            if last[1] < interval[0]:
                disjoint_intervals.append(interval)
            elif last[1] < interval[1]:
                new_interval = (last[0], interval[1])
                disjoint_intervals.pop()
                disjoint_intervals.append(new_interval)

    result = len(disjoint_intervals)
    return result


if __name__ == '__main__':
    A = [1, 12, 42, 70, 36, -4, 43, 15]
    B = [5, 15, 44, 72, 36, 2, 69, 24]
    solution(A, B)
