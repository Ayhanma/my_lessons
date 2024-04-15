import sqlite3
con = sqlite3.connect("bank.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bank
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               surname TEXT,
               age INTEGER,
               password TEXT)''')
while True:
    ans = input('Хотите ли вы зарегестрироваться:')
    if ans.lower() == 'да':
        name = input('Input your name:')
        surname = input('Input your surname:')
        age = input('Input your age:')
        password = input('Input tour password:')
        data = (name,surname,age,password)
        cursor.execute('INSERT INTO bank(name,surname,age,password) VALUES(?,?,?,?)', data )
        con.commit()
    else:
        answ = input('У вас есть логин:')
        if answ == 'Да' or answ == 'да':
            login = input('Введите ваш логин:')
            passw = input('Введите ваш пароль:')
            cursor.execute("SELECT WHERE name = (?) FROM bank", login)
            for i in cursor.fetchall():
                print(i)
                # if i[1] == login and i[4] == passw:
                #     print('Welcome')
                # else:
                #     print('Error try again')
                            
                        