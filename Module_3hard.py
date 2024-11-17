sum_num = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    global sum_num
    for i in data_structure:
        if isinstance(i, int):
            sum_num += i
        elif isinstance(i, str):
            sum_num += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)  # Если встретили коллекцию, вызываем эту же функцию с этой коллекцией
        elif isinstance(i, dict):
            for j in i:  # j - ключ словаря
                if isinstance(j, str):  # Проверка ключа
                    sum_num += len(j)
                elif isinstance(j, int):
                    sum_num += j
                else:  # Если ключ кортеж
                    calculate_structure_sum(j)
                if isinstance(i[j], str):  # Проверка значения по ключу
                    sum_num += len(i[j])
                elif isinstance(i[j], int):
                    sum_num += i[j]
                else:
                    calculate_structure_sum(i[j])
    return sum_num


result = calculate_structure_sum(data_structure)
print(result)