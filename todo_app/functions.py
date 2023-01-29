def get_todos(filepath="files_todo/todos.txt") -> object:
    """ reads a text file and returns list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files_todo/todos.txt"):
    """ writes the to-do list, to a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)