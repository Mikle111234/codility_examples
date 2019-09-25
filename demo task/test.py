def solution(A):
    b = set(A)
    print(b)
    result = 0
    for i in range(1, len(b)+2):
        if i in b:
            continue
        else:
            result = i
            break
    print(result)
    return result


if __name__ == '__main__':
    A = [1, 0, 3, 4]
    solution(A)
