from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            list_string = f"{index + 1}. {item}"
            print(list_string)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Please enter the number of todo after edit.")
            continue
        except IndexError:
            print("Out of range of ToDo list. Try again.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            complete_todo = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            complete_message = f"todo: {complete_todo} was removed from the list."
            print(complete_message)
        except IndexError:
            print("Out of range of ToDo list. Try again.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown command, Please try again.")

print("Goodbye!")
