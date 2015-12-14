

def palindrom(s):
    a, b = 0, len(s)-1
    while a < b:
        if s[a] == s[b]:
            a += 1
            b -= 1
        else:
            return False
    return True


def find(s, b, e):
    result = s[b:e]

    while e < len(s):
        b += 1
        e += 1
        if palindrom(s[b:e]):
            while (b > 0) and (e < len(s)) and (s[b-1] == s[e]):
                b -= 1
                e += 1
            result = s[b:e]

    return result


if __name__ == '__main__':
    s = raw_input()
    p1 = find(s, 0, 1)
    p2 = find(s, 0, 2)

    print (p1 if len(p1) >= len(p2) else p2)
