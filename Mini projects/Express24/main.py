import datetime
import json

from tabulate import tabulate


def read_file(filename):
    try:
        with open(filename, 'r') as read_users:
            data = json.load(read_users)
        return data
    except FileNotFoundError:
        print('File not found...')


def write_file(filename, data):
    with open(filename, 'w') as write_users:
        json.dump(data, write_users, indent=4)


def register():
    fullname = input('Enter your name: ')
    username = input('Enter your username: ')
    data = read_file('users.json')
    for user in data:
        if user['username'] == username:
            print('This user already...')
            return
    role_list = ['user', 'kuryer', 'company']
    print(role_list)
    role = int(input('Role: '))
    if role_list[role - 1] == 'kuryer':
        password = input('Password: ')
        r_date = str(datetime.datetime.now())
        data.append({'id': data[-1]['id'] + 1, 'fullname': fullname, 'username': username, 'role': role_list[role - 1],
                     'orders': [], 'history': [],
                     'is_user': False, 'password': password, 'r_date': r_date, 'chats': []})
        print('Arizangiz qabul qilindi...')
        print("Tez orada javob beriladi...")

    elif role_list[role - 1] == 'company':
        password = input('Password: ')
        r_date = str(datetime.datetime.now())
        data.append({'id': data[-1]['id'] + 1, 'fullname': fullname, 'username': username, 'role': role_list[role - 1],
                     'products': [], 'history': [],
                     'is_user': False, 'password': password, 'r_date': r_date, 'chats': []})
        print('Arizangiz qabul qilindi...')
        print("Tez orada javob beriladi...")
    else:
        password = input('Password: ')
        r_date = str(datetime.datetime.now())
        data.append({'id': data[-1]['id'] + 1, 'fullname': fullname, 'username': username, 'role': role_list[role - 1],
                     'history': [], 'password': password, 'r_date': r_date, 'chats': []})
    write_file('users.json', data)

    print('Saqlandi..')
    login()


def user_list():
    data = read_file('users.json')
    header, l = ['Id', 'username', 'Full name', 'Role', 'Allow', 'Password', 'Date'], []
    for i in data:
        if i['role'] == 'user':
            l.append([i['id'], i['username'], i['fullname'], i['role'], 'Not allowed', i['password'], i['r_date']])
        else:
            l.append([i['id'], i['username'], i['fullname'], i['role'], i['is_user'], i['password'], i['r_date']])

    print(tabulate(l, headers=header, tablefmt='psql'))


# Ruxsat berish
def allowed_users():
    data = read_file('users.json')
    user_list()
    while True:
        print('0. Save / Exit')
        n = int(input('Enter username id: '))
        match n:
            case 0:
                break
            case _:
                if len(data) >= n:
                    print('1. Allowed\t2. Not allowed')
                    for i in data:
                        if i['id'] == n and i['role'] != 'user':
                            i['is_user'] = True
                            print('Allow to user...')

                else:
                    print('This is not a valid')

                write_file('users.json', data)
                user_list()
    print('Allowed and Saved')


# allowed_users()

def userpage(user):
    menu = """1. Give orders\n2. My orders\n3. History\n4. My account\n0. Exit"""
    while True:
        print(menu)
        n = int(input('Enter menu: '))
        match n:
            case 1:
                pass
            case 2:
                pass
            case 3:
                print(*[i for i in user['history']])
            case 4:
                pass
            case 0:
                print('Good bye')
                break
            case _:
                continue


def login():
    username = input('Username: ')
    password = input('Password: ')
    for i in read_file('users.json'):
        if i['username'] == username and i['password'] == password and i['role'] == 'user':
            print('User list')
            i['history'].append(f'Siz {datetime.datetime.now()} saytga kirdingiz')
            write_file('users.json', read_file('users.json'))
            userpage(i)
            break
        elif i['username'] == username and i['password'] == password and i['role'] == 'kuryer':
            print('Kuryer list')
            if i['is_user']:
                print('Xush kelibsiz!!!')
            else:
                print('Admin javobini kuting')
            break
        elif i['username'] == username and i['password'] == password and i['role'] == 'company':
            print('Company list')
            if i['is_user']:
                print('Xush kelibsiz!!!')
            else:
                print('Admin javobini kuting')
            break
        elif i['username'] == username and i['password'] == password and i['role'] == 'admin':
            print('Admin list')
            break
    else:
        print('This is not find')
        register()

login()