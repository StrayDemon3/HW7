db_list = []  

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
            my_list = file.readlines()
            for line in my_list:
                id_dict = dict()
                line = line.strip().split(';')
                id_dict['lastname'] = line[0]
                id_dict['firstname'] = line[1]
                id_dict['phone'] = line[2]
                id_dict['comment'] = line[3]
                db_list.append(id_dict)

def exit_program():
    exit()

def save_file(db, path: str):
    new_text = ''
    for item in db:
        new_text += item.get('lastname') + '; '
        new_text += item.get('firstname') + '; ' 
        new_text += item.get('phone') + '; '
        new_text += item.get('comment') + '; ' + '\n'

    with open(path, 'w', encoding='UTF-8') as file:
        file.writelines(new_text)


def del_contact(user_del):
    global db_list
    db_list.pop(user_del - 1)

def find_contact(inp_find):
    global db_list
    result = ''
    
    for i in range(len(db_list)):
        if db_list[i].get('lastname') == inp_find or \
            db_list[i].get('firstname') == ' ' + inp_find or \
            db_list[i].get('phone') == ' ' + inp_find or \
            db_list[i].get('comment') == ' ' + inp_find:
            result += db_list[i]['lastname']\
                + db_list[i]['firstname']\
                + db_list[i]['phone']\
                + db_list[i]['comment'] + '\n' + '\t'
            return result
        elif result  == '':
            return None

def show_all():
    global db_list
    for i in range(len(db_list)):
        user_id = i + 1
        print(f'\t {user_id}', end='.')
        for v in db_list[i].values():
            print(f'{v}', end=' ')
        print('')