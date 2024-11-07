import re

class file_job:
    def print_and_add_and_enter(self):
        word = input('Введите своё слово для добавления в файл: ')
        with open("file.txt", "a") as file:
            file.write(word + '\n')
        
        print('Слова в файле: ')
        with open("file.txt", "r") as file:
            print(file.read())

    def check(self):
        count = 0
        try:
            with open('file.txt', 'r') as file:
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
                if re.match(r"\b(\w+)\1\b", list_word[i]):
                    print("Тандемный повтор пренадлжеит этому слову: " + list_word[i])
