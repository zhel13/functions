def concatenate(*args, **kwargs):
    result = ""
    for i in args:
        result += i
    for k, v in kwargs.items():
        while k in result:
            result = result.replace(k, kwargs[k])
    return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
