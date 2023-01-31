FILEPATH = "files_todo/todos.txt"


def get_todos(filepath=FILEPATH) -> object:
    """ reads a text file and returns list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ writes the to-do list, to a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
