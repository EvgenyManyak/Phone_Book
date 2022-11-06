import view
import os

def get_add():
    list = ['Фамилию: ','Имя: ','номер телефона: ','коментарий']
    data = view.get_input(list)
    with open('people.csv', 'a') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')

def get_see():
    with open('people.csv', 'r') as file:
        data = []
        data = file.readlines()
        print(''.join(data))

def get_find():
    with open('people.csv', 'r') as file:
        data = []
        data_see = []
        data = file.readlines()
        text = input('Введите слово для поиска: \n')
        for i in range(len(data)):
            data[i] = ''.join(data[i])
            row = []
            row = data[i]
            if text in row:
                print(f'№ {i+1} : {row}')
        

def get_del():
    with open('people.csv', 'r') as file:
        data = []
        data = file.readlines()
        print('-'*100)
        for i in range(len(data)):
            print(f'№ {i+1} : {data[i]}')
        oper = int(input('Удалить контакт \n1 - да \n2 - нет \nВвод: ')) 
        if oper == 1: 
            number = int(input('Введите номер контакта для удаления: '))
            n = number-1
            data.pop(n)
            data = ''.join(data)
            print(f'Вы удалили контакт № {number}')
            with open('people.csv', 'w') as file:
                file.writelines(f'{data} \n')
        elif oper == 2: 
            False
        else:
            False    

def get_del_find():
    with open('people.csv', 'r') as file:
        data = []
        data_see = []
        data = file.readlines()
        data_new = []
        text = input('Введите слово для поиска: \n')
        for i in range(len(data)):
            data[i] = ''.join(data[i])
            row = []
            row = data[i]
            if text in row:
                print(f'N {i+1} удалить? : {row}')
                data_new.append(row)     
        oper = int(input('Удалить найденные записи \n1 - да \n2 - нет \nВвод: ')) 
        if oper == 1: 
            data_del = comp(data,data_new)
            data_del = ''.join(data_del)
            with open('people.csv', 'w') as file:
                file.writelines(f'{data_del} \n')
        elif oper == 2: 
            False
        else:
            False

def comp(a,b):
    return list(set(a)-set(b))