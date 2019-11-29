"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
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
    print(chating())
    
if __name__ == "__main__":
    ask_user()
