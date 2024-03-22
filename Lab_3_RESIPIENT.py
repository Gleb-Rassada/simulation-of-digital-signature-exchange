from tkinter import *
import tkinter as ttk


class WinResipient(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.config(bg ="#cde5ff")
        self.title("окно граф приложения") # название главного окна
        self.geometry("550x400+820+0") # указал размер окна и плюсами место его появления
        self.resizable(False,False) # запретил изменять размер окна по длинне и ширине

        self.resipientLabel = ttk.Label(self, text='Получатель',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=5,
                    width= 15,
                    height=0
                   )

        self.buttonFun1 = ttk.Button(self, text="функция 1",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    )

        self.buttonFun2 = ttk.Button(self, text="функция 2",
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
                    command=self.button_close,
                   )
        
        self.resipientLabel.pack(anchor="n",pady=[30,80])
        self.buttonFun1.pack(anchor="n",pady=[0,15])
        self.buttonFun2.pack(anchor="n",pady=[0,15])
        self.closeButton.pack(anchor="n",pady=[0,15])

# Функционал кнопок
    def button_close(self):
        self.destroy()

