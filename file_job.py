import re

class file_job:
    def print_and_add_and_enter(self):
        word = input('Введите своё слово для добавления в файл: ')
        
        with open("file.txt", "a") as myfile:
            myfile.write(word)
        
        

    def check(self):
        print('check')