from file_job import file_job

def menu():
    file = file_job()
    command = ''
    print('Выберите, пожалуйста, команду из нижеперечсиленных:')
    print('1. Ввод слова и его добавление в файл.')
    print('2. Проверка слов в файле через регулярное выражение.')
    print('3. Выход.')
    while (command != '3'):
        command = input("Введите номер команды: ")
        if command == '1':
            file.print_and_add_and_enter()
        elif command == '2':
            file.check()
        elif command == '3':
            print('Вы вернулись в начальное меню.')
        else:
            print('Неверный ввод.')

main = ''
while(main != '2'):
    main = input("Напишите '1', если хотетите войти в главное меню, и '2', если хотите завершить работу: ")
    if main == '1':
        menu()
    elif main == '2':
        print('До свидания!')
    else:
        print('Неверный ввод.')