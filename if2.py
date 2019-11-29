"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    def is_number(string1, string2):
        try:
            float(string1) and float(string2)
            return "Это цифровые значения"
        except ValueError:
            return "Текст"
    def compare(string1, string2):
        if string1 == string2:
            return "1 - Совпадают"
        elif string1 != string2:
            return "Не совпадают"
        else:
            return "null"
    def len_string(string1, string2):
        if len(string1) == len(string2):
            return "2 - одинаковая длина"
        elif len(string1) != len(string2):
            return "Разная длина"
    def search_learn(string1, string2):
        if string1 != string2 and string2 == 'learn':
            return "3 - learn есть"
        else:
            return "learn отсутствует"


    string1, string2 = (input() for _ in range(2))
    print(is_number(string1,string2))
    print(compare(string1,string2))
    print(len_string(string1,string2))
    print(search_learn(string1,string2))
    
if __name__ == "__main__":
    main()
