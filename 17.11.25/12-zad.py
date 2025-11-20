for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b and b != c and a != c:
                if a + b + c == 15:
                    print(a, b, c)
