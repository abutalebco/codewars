def tower_builder(n):
    arr = []
    for i in range(n):
        arr.append(" " * (n - 1 - i) + "*" * (2 * i + 1) + " " * (n - 1 - i))
    return arr