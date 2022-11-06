import func
import view
import log

def directory():
    oper = int(input('01 - Добавить контакт \n02 - Удалить контакт \n03 - Найти контакт \n04 - Показать все контакты \n05 - Удаление по поиску \n06 - Выход \nВведите, что вы хотите сделать 1-6: '))
    while oper <= 6:
        if oper == 1:
            log.input_write('Добавили контакт')
            func.get.add()
        elif oper == 2:
            log.input_write('Удалили контакт')
            func.get_del()
        elif oper == 3:
            log.input_write('Выполнили поиск контакта')
            func.get_find()
        elif oper == 4:
            log.input_write('Демонстрация телефонной книги')
            func.get_see()
        elif oper == 5:
            log.input_write('Удалили поисковую информацию')
            func.get_del_find()
        if oper == 6:
            print('Спасибо, что выбрали наш продукт')
            break
        oper = int(input('01 - Добавить контакт \n02 - Удалить контакт \n03 - Найти контакт \n04 - Показать все контакты \n05 - Удаление по поиску \n06 - Выход \nВведите, что вы хотите сделать 1-6: '))



