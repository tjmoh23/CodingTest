a, b = map(str, input().split())

def word_len(a, b):

    len_a = len(a)
    len_b = len(b)

    if len_a > len_b:
        print(a)
    else:
        print(b)
    return

word_len(a, b)