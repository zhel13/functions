def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == "even":
            kwargs[k] = [int(x) for x in v if x % 2 == 0]
        if k == "odd":
            kwargs[k] = [int(x) for x in v if x % 2 != 0]
    ordered = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    new_result = {}
    for i in ordered:
       new_result[i[0]] = i[1]
    return new_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
