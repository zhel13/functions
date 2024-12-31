def func_executor(*func_data):
    result = []
    for name, arg in func_data:
        result.append(f"{name.__name__} - {name(*arg)}")
    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)),(multiply_numbers, (2, 4))
))
