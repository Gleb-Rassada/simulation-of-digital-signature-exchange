from Cryptodome.Hash import SHA1
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
import os

def hash_file_sha1():
    print('введите имя файла который нужно хэшировать')
    fileName=input()
    with open(fileName, 'rb') as f:   #f-file
        sha1Hash = SHA1.new()
        while True:             #записывает блоками по 8192 байта файл в переменную
            data = f.read(8192) 
            if not data:
                break
            sha1Hash.update(data)      # update - записывает(приплюсовывает) в переменную данные
        return sha1Hash

def sender():
    print("---------------------------------------")
    print("ОКНО ОТПРАВИТЕЛЯ")


    print("---------------------------------------")
    #выбрать файл
    #отправить файл нотариусу

def notary():
    print("---------------------------------------")
    print("ОКНО НОТАРИУСА")


    print("---------------------------------------")
    #создаёт ключи

def recipient():
    print("---------------------------------------")
    print("ОКНО ПОЛУЧАТЕЛЯ")


    print("---------------------------------------")
    #

while True:
        print ("Чтобы получить электронную подпись нажмите: '1'")
        print ("Чтобы закрыть программу введите: 'exit'")
        useChoice = input()
        if useChoice == 'exit':
            break
        elif useChoice == '1':
            # Генерация ключа
            key = RSA.generate(1024, os.urandom)
            # Получение хэш файла
            sha1Hash = hash_file_sha1()
            # Подписываем хэш
            signature = pkcs1_15.new(key).sign(sha1Hash)
            # Получаем открытый ключ из закрытого
            pubKey = key.publickey()
            print ("Чтобы получить проверить подлинность введите: '2'")
            useChoice = input()
            if  useChoice == '2':
                # верификация подписи
                try:
                # верификация происходит путём использования 
                # открытого ключа, хэша файла и подписи
                    pkcs1_15.new(pubKey).verify(sha1Hash, signature) 
                    print ("The signature is valid.")
                    print(signature)
                except (ValueError, TypeError):
                    print ("The signature is not valid.")
            else:
                print()
        else: 
            print('Некорректный ввод - попробуйте снова')

while True:
    useChoice = input()
    if useChoice == 'exit':
        break
    elif useChoice == '1':
        print("Отправитель") #sender
        
    elif useChoice == '2':
        print("Нотариус") #notary

    elif useChoice == '3':
        print("Получатель") #recipient
