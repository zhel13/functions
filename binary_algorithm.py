def binary_alg(desired_num, data_base):
    left = 0
    right = len(data_base) - 1

    while left <= right:
        middle_element = (left + right) // 2
        mid_num = data_base[middle_element]
        if mid_num == desired_num:
            return middle_element
        if mid_num < desired_num:
            left = middle_element + 1
        else:
            right = middle_element - 1

des = int(input())
data_b = [int(x) for x in input().split()]
result = binary_alg(des, data_b)
print(result)