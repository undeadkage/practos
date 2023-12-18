password = input ('пароль')
login = input ('логин')
file = open('auth.txt', 'w')
file.write('1)логин: '+ login )
file.write('2)пароль: '+ password )
with open("auth.txt") as file:
    print('Данные записаны в файл auth.txt ')