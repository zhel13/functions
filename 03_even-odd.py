def even_odd(*args):
    mapper = {
        "even": [int(x) for x in args[0:-1] if x % 2 == 0],
        "odd": [x for x in args[0:-1] if x % 2 != 0]
    }

    return mapper[args[-1]]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))