
num1 = map(lambda n: int(n) - int('0'),list(raw_input()))
num2 = map(lambda n: int(n) - int('0'),list(raw_input()))

num1.reverse()
num2.reverse()


def normalize(n):
    c = 0
    for i in range(len(n)):
        n[i] += c
        n[i], c = (n[i] % 10), (n[i] // 10)

    while c > 0:
        n.append(c % 10)
        c = c // 10

def do_sum(n1, n2):
    l1 = len(n1)
    l2 = len(n2)

    if l1 < l2:
        nn1 =  n1 + [0 for i in range(l2-l1+1)]
    else:
        nn1 = n1

    if l1 > l2:
        nn2 = n2 + [0 for i in range(l1-l2+1)]
    else:
        nn2 = n2

    res = [nn1[i]+nn2[i] for i in range(len(nn1))]
    normalize(res)
    return res

def do_mul(n1, n2):
    res = [0 for i in (n1+n2)]

    for i, d1 in enumerate(n1):
        for j, d2 in enumerate(n2):
            res[i+j] += d1 * d2

    normalize(res)
    return res

def do_print(n):
    m = n[:]
    m.reverse()
    print("".join([str(c) for c in m]))

if raw_input().strip() == "+":
    do_print(do_sum(num1, num2))
else:
    do_print(do_mul(num1, num2))
