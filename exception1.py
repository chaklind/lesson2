"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    chat_dictonary =  {'Как дела?' : 'Хорошо!' , "Что делаешь?": "Программирую"} 


    def chating():
            while True:
                user_say = input()
                if user_say == "Как дела?":
                    print(chat_dictonary["Как дела?"])
                    user_say = input()
                    if user_say == "Что делаешь?":                
                        print(chat_dictonary["Что делаешь?"])   
                        break                      
                    else:
                        print('Сам ты {}'.format(user_say))               
                else:
                    print('Сам ты {}'.format(user_say))


    try:
        print(chating())
    except KeyboardInterrupt:
        print("Пока")
    
if __name__ == "__main__":
    ask_user()
