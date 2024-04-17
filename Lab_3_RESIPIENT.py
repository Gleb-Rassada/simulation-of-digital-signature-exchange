from tkinter import *
import tkinter as ttk
from Cryptodome.Hash import SHA1
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
import os

class WinResipient(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.config(bg ="#cde5ff")
        self.title("окно граф приложения") # название главного окна
        self.geometry("650x400+820+0") # указал размер окна и плюсами место его появления
        self.resizable(False,False) # запретил изменять размер окна по длинне и ширине

        self.resipientLabel = ttk.Label(self, text='Получатель',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=3,
                    width= 15,
                    height=0
                   )
        self.resipientEntryLabel = ttk.Label(self, text="Введите название файла для проверки",
                    bg = "white",
                    fg = "black",
                    font=('Arial',18,'bold'),
                    pady=1,
                    width=40, 
                    height=0,
                    )
        self.entry = ttk.Entry(self)

        self.buttonFun1 = ttk.Button(self, text="Проверка на подлинность",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    command= self.proverkaNaPodlinnost
                    )

        self.verifiedLabel = ttk.Label(self, text='-----',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=5,
                    width= 25,
                    height=0
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
        
        self.resipientLabel.pack(anchor="n",pady=[30,40])
        self.resipientEntryLabel.pack(anchor="n",pady=[10,10])
        self.entry.pack(anchor="n",pady=[0,20])
        self.buttonFun1.pack(anchor="n",pady=[0,15])
        self.verifiedLabel.pack(anchor="n",pady=[0,13])
        self.closeButton.pack(anchor="n",pady=[0,15])


# Функционал кнопок
    
    def button_close(self):
        self.destroy()
 
    def proverkaNaPodlinnost(self):
        os.chdir('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/RESIPIENTS_FOLDER') #директория с которой работаем в данный момент
        recipientsFolderPath = ('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/RESIPIENTS_FOLDER/')
        fileName = os.path.join(recipientsFolderPath,self.entry.get())
        self.entry.delete(0,END)
        with open(fileName, 'rb') as f:   #f-file
            sha1Hash = SHA1.new()
            while True:             #записывает блоками по 8192 байта файл в переменную
                data = f.read(8192) 
                if not data:
                    break
                sha1Hash.update(data) 

        pubKeyPath = "/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/RESIPIENTS_FOLDER/public_key.pem"
        signaturePath = "/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/RESIPIENTS_FOLDER/signature"
        # верификация подписи
        try:
        # верификация происходит путём использования 
                # открытого ключа, хэша файла и подписи
            with open (pubKeyPath, "rb") as pubKeyFromFile:
                pubKey = RSA.import_key(pubKeyFromFile.read())
            with open (signaturePath, "rb") as f:
                signature = f.read()
            pkcs1_15.new(pubKey).verify(sha1Hash, signature) 
            self.verifiedLabel.config(text='файл подлинный')
        except (ValueError, TypeError):
            self.verifiedLabel.config(text='файл не подлинный')


