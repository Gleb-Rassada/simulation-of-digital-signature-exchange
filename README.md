Стоит потом как-нибудь довести эту програмку до ума, чтобы её можно было запускать через exe и на любом ПК (сделать адаптируемые директории)
но займусь я этим не сегодня и не завтра), так как практической ценности эта программа больше для меня не имеет.

Структура и функционал программы:
Главное меню:
1.) Отправитель
2.) Нотариус
3.) Получатель
4.) Выход (из программы)

Отправитель имеет функции:
1.) Отправить файл который нужно подписать нотариусу. (file)
2.) Отправить 2 файла получателю подписанный или не подписанный. (file, signedFile)
3.) Выход в меню
 
Функции нотариуса:
1.) Создать ключи 
2.) Подписать документ ЗК и ХЭШ - получили подпись и положить её в файл 'signature'
3.) Отправить подписанный документ отправителю (signedFile)
4.) Отправить signature и openKey получателю
5.) Выход в меню

Функция получателя:
Имея документы file, signed_file (Лежащие в папке Resipient), и signedFile, openKey -> проверить подлинность документов
1.) проверяем file
2.) проверяем signedFile
3.) Выход в меню
