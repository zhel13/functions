def grocery_store(**kwargs):
    result = {}
    final_result = []
    el = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for i in el:
        result[i[0]] = i[1]

    for k, v in result.items():
        final_result.append(f'{k}: {v}')

    return '\n'.join(final_result)



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
