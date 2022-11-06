import tkinter as tk
import interface, func


def createAddWindow():
    global add_window
    global entry_name
    global entry_last_name
    global entry_phone
    global entry_comment

    add_window = tk.Toplevel()
    add_window.title('Добавить контакт')
    add_window.geometry('400x240')
    add_window.resizable(0,0)


    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    add_window.mainloop()

    