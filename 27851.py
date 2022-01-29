for n in range(210235, 210300 + 1):
    a = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            a.append(d)
            if len(a) > 4:
                break
    if len(a) == 4:
        print(a[0], a[1], a[2], a[3])


