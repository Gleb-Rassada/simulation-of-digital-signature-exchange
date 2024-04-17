from tkinter import *
import tkinter as ttk
import Lab_3_NOTARY
import Lab_3_RESIPIENT
import Lab_3_SENDER


mainWin = ttk.Tk() #создал объект главного окна
# background = tk.PhotoImage(file = 'background1.jpg')
mainWin.config(bg ="#cde5ff")
# mainWin.iconphoto(False, winIcon)
mainWin.title("окно граф приложения") # название главного окна
mainWin.geometry("650x400+820+0") # указал размер окна и плюсами место его появления
mainWin.resizable(False,False) # запретил изменять размер окна по длинне и ширине

# функция закрытия
def exitBtn():
    mainWin.destroy()


label_1 = ttk.Label(mainWin, text='Меню',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=5,
                    width= 15,
                    height=0
                   )

buttonSender = ttk.Button(mainWin, text="Отправитель",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=15, 
                    height=0,
                    command=Lab_3_SENDER.WinSender,
                    )

buttonRecipient = ttk.Button(mainWin, text="Получатель",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=15, 
                    height=0,
                    command=Lab_3_RESIPIENT.WinResipient,
                    )

buttonNotary = ttk.Button(mainWin, text="Нотариус",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=15, 
                    height=0,
                    command=Lab_3_NOTARY.WinNotary,
                    )

# кнопка закрытия
buttonClose = ttk.Button(mainWin, text="Выход",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=15, 
                    height=0,
                    command=exitBtn,
                    )


label_1.pack(anchor="s",   #располагает лейбл на окне
             pady=[30,40]) #настроил падинги по y

buttonSender.pack(anchor="s",
              pady=[0,15])

buttonNotary.pack(anchor="s",
              pady=[0,15]) 
 
buttonRecipient.pack(anchor="s",
              pady=[0,15]) 

buttonClose.pack(anchor="s",
              pady=[0,15]) 

mainWin.mainloop() # так называемый главный цикл содержащий главное окно
# Главное меню:
# 1.) Отправитель
# 2.) Нотариус
# 3.) Получатель
# 4.) Выход (из программы)

# Отправитель имеет функции:
# 1.) Отправить файл который нужно подписать нотариусу. (file)
# 2.) Отправить 2 файла получателю подписанный или не подписанный. (file, signedFile)
# 3.) Выход в меню
 
# Функции нотариуса:
# 1.) Создать ключи 
# 2.) Подписать документ ЗК и ХЭШ - получили подпись и положить её в файл 'signature'
# 3.) Отправить подписанный документ отправителю (signedFile)
# 4.) Отправить signature и openKey получателю
# 5.) Выход в меню

# Функция получателя:
# Имея документы file, signed_file (Лежащие в папке Resipient), и signedFile, openKey -> проверить подлинность документов
# 1.) проверяем file
# 2.) проверяем signedFile
# 3.) Выход в меню
 
# скэпи или скапи - библиотека для отправки пакетов