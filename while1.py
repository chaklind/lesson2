"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    def chating():
        while True:
            print("Как дела?")
            user_say = input()
            if user_say == "Хорошо":
                break          
            else:
                print('Сам ты {}'.format(user_say))
    print(chating())

    
if __name__ == "__main__":
    ask_user()



