from functools import reduce


def math_operations(*args, **kwargs):
    to_print = []

    for i in range(len(args)):
        keys = list(kwargs.keys())[i % 4]
        if keys == "a":
            kwargs[keys] += args[i]
        elif keys == "s":
            kwargs[keys] -= args[i]
        elif keys == "d":
            if args[i] == 0:
                continue
            else:
                kwargs[keys] /= args[i]
        elif keys == "m":
            kwargs[keys] *= args[i]
    result = (sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

    for i in range(len(result)):
        k = result[i][0]
        v = result[i][1]
        to_print.append(f"{k}: {v:.1f}")
    return "\n".join(to_print)


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))