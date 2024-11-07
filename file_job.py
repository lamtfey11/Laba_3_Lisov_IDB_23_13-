import re

class file_job:
    def print_and_add_and_enter(self):
        word = input('Введите своё слово для добавления в файл: ')
        word += "\n"
        with open("file.txt", "a") as file:
            file.write(word)
        
        with open('file.txt', 'r') as file:
            print(file.read())

    def check(self):
        print('check')