def get_input(lst):
    data = []
    for i in lst:
        print(f'\n Введите {i}')
        data.append(input())
    return data