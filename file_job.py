import re

class file_job:
    def print_and_add_and_enter(self, name):
        word = input('Введите своё слово для добавления в файл: ')
        with open(name, "a") as file:
            file.write(word + '\n')
        
        print('Слова в файле: ')
        with open("file.txt", "r") as file:
            print(file.read())
        

    def check(self, name):
        count = 0
        try:
            with open(name, 'r') as file:
                print(file.read())
                count = 1
        except FileNotFoundError:
            print("Файл numbers.txt не существует.")
        if count == 1:
            with open("file.txt", "r", encoding="utf-8") as file:
                list_words_beta = file.readlines()
            
            list_word = list()
            for i in range(len(list_words_beta)):
                list_word.append(list_words_beta[i][:len(list_words_beta[i]) - 1])
                
            for i in range(len(list_word)):
                w = list_word[i]
                R(w)

def R(word):
    if word == word.replace(" ", ""):
        if re.findall(r"\b(\w+)\1\b", word):
            print("Тандемный повтор пренадлжеит этому слову: " + word)
            return True
        else:
            return False
    else:
        res = re.findall(r"\b(\w+)\1\b", word)
        if res:
            for i in range(len(res)):
                res[i] = res[i] * 2
            print("Тандемный повтор сущетвует в подстроках этой строки: " + word + f" - а именно: {res}")
            return True
        else:
            return False