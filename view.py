def main_menu() -> int:
    print('Главное меню: ')
    menu_list = ['Открыть файл',
                'Сохранить файл',
                'Показать все контакты',
                'Создать контакт',
                'Изменить контакт',
                'Найти контакт',
                'Удалить контакт',
                'Выход'
                ]
    for i in range(len(menu_list)):
        print(f'\t{i+1}. {menu_list[i]}')
    while True:
        try:
            user_input = input('Введите команду: ')
            user_input = int(user_input)
            break
        except ValueError: 
            print('Команда определяется цифрой')
    return user_input
    
def open_file():
        print('Файл открыт')

def db_success(db: list):
    if db:
        print('Телефонная книга: ')
        return True
    else:
        print('Телефонная книга пуста или не открыта')

def exit_program():
    print('Завершение программы')

def create_contact(db):
    # if db_success(db):
        print('Создайте новый контакт:')
        new_contact = {}

        new_contact['lastname'] = input('Введите фамилию: ')
        new_contact['firstname'] = input('Введите имя: ')
        new_contact['phone'] = input('Введите номер телефона: ')
        new_contact['comment'] = input('Введите комментарий: ')
        return new_contact

def change_contact(db):
    try:
        id_change = int(input('Введите id контакта, котороый хотите изменить: '))
        if id_change <= len(db):
            menu_change = ['1. Фамилия',
                '2. Имя',
                '3. Номер телефона',
                '4. Комментарий']
            print(menu_change)
            user_inp = int(input('Введите параметр для изменения: '))
            match user_inp:
                case 1:
                    db[id_change-1]['lastname'] = input('Введите фамилию: ')
                case 2:
                    db[id_change-1]['firstname'] = input('Введите имя: ')                
                case 3:
                    db[id_change-1]['phone'] = input('Введите номер телефона: ')
                case 4:
                    db[id_change-1]['comment'] = input('Введите комментарий: ')

    except ValueError:
        print('Введено не верное значение id контакта')

def error_adding_contact():
    print('Ошибка добавления контакта')

def del_contact():
    user_del = int(input('Введите номер контакта, который хотите удалить: '))
    return user_del

def find_contact():
    inp_find = input('Введите данные для поиска контакта: ')
    return inp_find

def search_completed(new_str: str):
    print(f'Результат поиска:\n\t{new_str}')

def no_contact():
    print('\tКонтакт не найден')

def file_is_clear():
    print('Телефонная книга пуста или не открыта')