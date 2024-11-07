import re

class file_job:
    def print_and_add_and_enter(self, name):
        word = input('Введите своё слово для добавления в файл: ')
        #открытие файла для добавления в него новой строки(слова)
        with open(name, "a") as file:
            file.write(word + '\n')
        
        print('Слова в файле: ')
        #открытие файла для чтения и для вывода строк в консоль
        with open("file.txt", "r") as file:
            print(file.read())
        

    def check(self, name):
        count = 0
        #проверка на пустоту файла
        try:
            #вывод содержимого файла
            with open(name, 'r') as file:
                print(file.read())
                count = 1
        except FileNotFoundError:
            print("Файл file.txt не существует.")
        if count == 1:
            #cодрежимое файла сохраняется в списке
            with open("file.txt", "r", encoding="utf-8") as file:
                list_words_beta = file.readlines()
            
            list_word = list()
            #сохраняем содрежимое списка без \n
            for i in range(len(list_words_beta)):
                list_word.append(list_words_beta[i][:len(list_words_beta[i]) - 1])
                
            for i in range(len(list_word)):
                w = list_word[i]
                R(w)

def R(word):
    #проверка на строку
    if word == word.replace(" ", ""):
        #проврека с помощью регулярного выражения
        if re.findall(r"\b(\w+)\1\b", word):
            print("Тандемный повтор пренадлжеит этому слову: " + word)
            return True
        else:
            return False
    else:
        #проврека с помощью регулярного выражения и сохранение в список слов
        res = re.findall(r"\b(\w+)\1\b", word)
        if res:
            for i in range(len(res)):
                res[i] = res[i] * 2
            print("Тандемный повтор сущетвует в подстроках этой строки: " + word + f" - а именно: {res}")
            return True
        else:
            return False