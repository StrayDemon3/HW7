import model
import view



def input_handler(user_inp: int, db):
    match user_inp:
        case 1:
            if db:
                view.open_file()
            else:
                view.open_file()
                model.read_db('database.txt')
        case 2: 
            model.save_file(model.db_list, 'database.txt')
        case 3:
            if view.db_success(model.db_list):
                model.show_all()
        case 4:
            new_contact = view.create_contact(model.db_list)
            if new_contact:
                model.db_list.append(new_contact)
            else:
                view.error_adding_contact()
        case 5:
            view.change_contact(model.db_list)
        case 6:
            inp_find = view.find_contact()
            res_find = model.find_contact(inp_find)
            if res_find:
                view.search_completed(res_find)
            else:
                view.no_contact()
        case 7:
            if model.db_list:
                model.del_contact(view.del_contact())
            else:
                view.file_is_clear()
        case 8:
            view.exit_program()
            model.exit_program()
        

def start_handler():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp, model.db_list)