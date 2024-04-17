from tkinter import *
import tkinter as ttk
import shutil
from Cryptodome.Hash import SHA1
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
import os

class WinNotary(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.config(bg ="#cde5ff")
        self.title("окно граф приложения") # название главного окна
        self.geometry("650x400+820+0") # указал размер окна и плюсами место его появления
        self.resizable(False,False) # запретил изменять размер окна по длинне и ширине

        self.notaryLabel = ttk.Label(self, text='Нотариус',
                    borderwidth=4,                    
                    bg ="#FFCDD2",
                    fg = "#B71C1C",
                    font=('Arial',22,'bold'),
                    pady=5,
                    width= 15,
                    height=0
                   )

        self.buttonFun1 = ttk.Button(self, text="Создать ключи",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    command= self.make_keys,
                    )

        self.buttonFun2 = ttk.Button(self, text="Подписать документ '1' ",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    command=self.make_a_signature
                    )
        
        self.buttonFun3 = ttk.Button(self, text="Рассылка адресатам",
                    bg = "white",
                    fg = "black",
                    font=('Arial',20,'bold'),
                    pady=1,
                    width=25, 
                    height=0,
                    command = self.send,
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
        
        self.notaryLabel.pack(anchor="n",pady=[30,40])
        self.buttonFun1.pack(anchor="n",pady=[0,15])
        self.buttonFun2.pack(anchor="n",pady=[0,15])

        self.buttonFun3.pack(anchor="n",pady=[0,15])
        self.closeButton.pack(anchor="n",pady=[0,15])

# Функционал кнопок
    def button_close(self):
        self.destroy()
    def send(self):
        signedFilePath = "/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/1_signed"
        signedFileDst = ('/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/SENDERS_FOLDER')
        shutil.copy(signedFilePath,signedFileDst)
        signaturePath ="/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/signature"
        recipientDST ="/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/RESIPIENTS_FOLDER"
        pubKeyPath="/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/public_key.pem"
        shutil.copy(signaturePath,recipientDST)
        shutil.copy(pubKeyPath,recipientDST)


    def make_keys(self):
        privKeyPath = '/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/private_key.pem'
        pubKeyPath = '/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/public_key.pem'
        privKey = RSA.generate(1024, os.urandom)
        
        with open(privKeyPath,'wb') as privKeyInFile:
                 privKeyInFile.write(privKey.export_key())

        pubKey = privKey.publickey()
        with open(pubKeyPath,'wb') as pubKeyInFile:
                 pubKeyInFile.write(pubKey.export_key())
        self.buttonFun2.pack(anchor="n",pady=[0,15])

    def hash_file_sha1(self):
        fileName='/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/1'
        with open(fileName, 'rb') as f:
            sha1Hash = SHA1.new()
            while True:        
                data = f.read(8192) 
                if not data:
                    break
                sha1Hash.update(data) 
        return sha1Hash

    def make_a_signature(self):

        sha1Hash = self.hash_file_sha1()

        privKeyPath = '/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/private_key.pem'
        signaturePath = '/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/signature'

        unsignedFilePath = "/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/1"
        signedFilePath = "/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/1_signed"


        with open(privKeyPath,'rb') as privKeyFromFile:
            privKey = RSA.import_key(privKeyFromFile.read())
        signature = pkcs1_15.new(privKey).sign(sha1Hash)
        with open(signaturePath,'wb') as signatureInFile:
            signatureInFile.write(signature)

        with open(unsignedFilePath,'rb') as f:
             signed1 = f.read()

        with open(signedFilePath,'wb') as f:
             f.write(signed1)

        pubKeyPath = '/home/gleb/Документы/IT_PROJECTS/NETWORK_DEFENCE_LABS/LAB_3/my_python_project/NOTARYS_FOLDER/public_key.pem'