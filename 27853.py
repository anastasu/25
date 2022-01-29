for n in range(312614, 312651 + 1):
    a = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            a.append(d)
            if len(a) > 6:
                break
    if len(a) == 6:
        print(a[0], a[1], a[2], a[3], a[4],a[5])
