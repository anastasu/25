for n in range(174457, 174505 + 1):
    a = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            a.append(d)
            if len(a) > 2:
                break
    if len(a) == 2:
        print(a[0], a[1])