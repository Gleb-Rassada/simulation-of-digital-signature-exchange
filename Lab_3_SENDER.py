from tkinter import *
import tkinter as ttk
import os
import shutil

# Отправитель имеет функции:
# 1.) Отправить файл который нужно подписать нотариусу. (file)
# 2.) Отправить 2 файла получателю подписанный или не подписанный. (file, signedFile)
# 3.) Выход в меню
 
class WinSender(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.config(bg ="#cde5ff")
        self.title("окно граф приложения") # название главного окна
        self.geometry("550x600+820+0") # указал размер окна и плюсами место его появления
        self.resizable(False,False) # запретил изменять размер окна по длинне и ширине

        self.entry = ttk.Entry(self)
        self.senderLabel = ttk.Label(self, text='Отправитель',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=5,
                    width= 15,
                    height=0
                   )
        
        self.senderEntryLabel = ttk.Label(self, text="Введите название файла",
                    bg = "white",
                    fg = "black",
                    font=('Arial',18,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    )


        self.buttonFun1 = ttk.Button(self, text="Отправить файл нотариусу",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    command=self.buttonSendToNotary
                    )




        self.buttonFun2 = ttk.Button(self, text="Отправить файл получателю",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    )
        

        self.closeButton = ttk.Button(self, text='Закрыть окно',
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=15, 
                    height=0,
                    command=self.buttonClose,
                   )

        
        self.senderLabel.pack(anchor="n",pady=[30,50])

        self.senderEntryLabel.pack(anchor="n",pady=[10,10])
        self.entry.pack(anchor="n",pady=[0,20])
        self.buttonFun1.pack(anchor="n",pady=[0,15])
        self.buttonFun2.pack(anchor="n",pady=[0,15])
        self.closeButton.pack(anchor="n",pady=[0,15])

# Функционал кнопок
    def buttonClose(self):
        self.destroy()
    
    def buttonSendToNotary(self):
        os.chdir('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/SENDERS_FOLDER') #директория с которой работаем в данный момент
        dst = ('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/NOTARYS_FOLDER')
        src = ('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/SENDERS_FOLDER/1')
        shutil.copyfile(src,dst)
        self.entry.delete(0,END)

 


