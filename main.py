def menu():
    print('menu')

main = ''
while(main != '0'):
    main = input("Напишите '1', если хотетите войти в главное меню, и '0', если хотите завершить работу.")
    if main == '1':
        menu()
    elif main == '0':
        print('До свидания!')
    else:
        print('Неверный ввод.')
    
