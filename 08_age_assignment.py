def age_assignment(*names, **age):
    result = []
    new_dict = {}
    for k, v in age.items():
        for i in names:
            if k == i[0]:
                new_dict[i] = v
    sorted_result = sorted(new_dict.items(), key=lambda x: x[0])
    for el in sorted_result:
        result.append(f"{el[0]} is {el[1]} years old.")
    return "\n".join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))