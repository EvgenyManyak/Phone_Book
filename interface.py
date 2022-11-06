from tkinter import *
from setuptools import Command
import controller
import func as f
from tkinter import Tk, Frame, Menu
from tkinter.ttk import Combobox
from tkinter import messagebox
import newwindows as nw

def text():
    id1 = Entry.get(entry_name)
    id2 = Entry.get(entry_last_name)
    id3 = Entry.get(entry_phone)
    id4 = Entry.get(entry_comment)
    with open('people.csv', 'a', encoding = 'utf8') as file:
        file.writelines(f'{id1}; {id2}; {id3}; {id4} \n')
def add():
        global window
        global entry_name
        global entry_last_name
        global entry_phone
        global entry_comment

        window = Toplevel()
        window.title('Добавить контакт')
        window.geometry('400x240')
        window.resizable(0,0)


        window.columnconfigure(index=0, weight=50)
        window.columnconfigure(index=1, weight=250)

        name_label = Label(window, text='Фамилия')
        last_name_label = Label(window, text='Имя')
        phone_label = Label(window, text='Телефон')
        comment_label = Label(window, text='Комментарий')

        name_label.grid(row=0, column=0, sticky = 'e')
        last_name_label.grid(row=1, column=0, sticky = 'e')
        phone_label.grid(row=2, column=0, sticky = 'e')
        comment_label.grid(row=3, column=0, sticky = 'e')

        entry_name = Entry(window)
        entry_last_name = Entry(window)
        entry_phone = Entry(window)
        entry_comment = Entry(window)

        entry_name.grid(row=0, column=1, sticky = 'w')
        entry_last_name.grid(row=1, column=1, sticky = 'w')
        entry_phone.grid(row=2, column=1, sticky = 'w')
        entry_comment.grid(row=3, column=1, sticky = 'w')

        btn = Button(window, text='Добавить',command = text)
        btn.grid(row=4, columnspan=2)
        window.mainloop()
    

def delete():
    f.get_del()

def find():
    f.get_find()

def see():
    with open('people.csv', 'r', encoding = 'utf8') as file:
        data_see = []
        data = file.readlines()
        for i in range(len(data)): 
            data_see.append(data[i])
    return data_see
                
def del_find():
        f.get_del_find()

def con():
    contacts = see()
    window = Tk()
    window.title("Контакты")
    window.geometry('640x480')
    for i in range(len(contacts)):
        id = contacts[i].split('; ')
        for j in range(len(id)):
            lbl = Label(window, text=id[j], font=("Helvetica", 12))
            lbl.grid(column=j, row=i)
    window.mainloop()

def start():  
    
    window = Tk()
    window.title("Добро пожаловать в приложение Телефонный справочник!")
    window.geometry('800x600')
    
    lbl = Label(window, text="Выберите действие:", font=("Helvetica", 14)).grid(columnspan=2, row=0)
    btn_add = Button(window, text = 'Создать контакт',font=("Helvetica", 12),command =add, height=1, width=25).grid(column= 1, row  = 1) 
    btn_del = Button(window, text = 'Удалить контакт',font=("Helvetica", 12),command =delete, height=1, width=25).grid(column= 1, row  = 2) 
    btn_find = Button(window, text = 'Найти контакт',font=("Helvetica", 12),command =find, height=1, width=25).grid(column= 1, row  = 3)
    btn_see =  Button(window, text = 'Вывести контакты',font=("Helvetica", 12),command = con, height=1, width=25).grid(column= 1, row  = 4) 
    btn_del_find = Button(window, text = 'Поиск и удаление',font=("Helvetica", 12),command =del_find, height=1, width=25).grid(column= 1, row  = 5)
    btn_exit = Button(window, text = 'Выход',font=("Helvetica", 12),command = False, height=1, width=25).grid(column= 1, row  = 6) 
      
    window.mainloop()