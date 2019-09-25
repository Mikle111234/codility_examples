import re


def solution1(S):
    pattern = r'\.|\?|\!'
    sentences_list = re.split(pattern, S)
    lens_of_sentences = []
    for sentence in sentences_list:
        s1 = sentence.split()
        lens_of_sentences.append(len(s1))
    result = max(lens_of_sentences)
    return result


def solution(S):
    pattern = r'\.|\?|\!'
    sentences_list = re.split(pattern, S)
    lens_of_sentences = [len(sentence.split()) for sentence in sentences_list]
    result = max(lens_of_sentences)
    return result


if __name__ == '__main__':
    # A = "We test coders. Give us a try?"
    A = "Forget  CVs..Save time . x x"
    solution(A)
