def get_todos(filepath):
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    return


while True:
    #Get user input and strip space chars from it.
    user_action = input("type add, show, edit or exit")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(filepath="todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt", todos_arg=todos)

    elif user_action.startswith("show"):

        todos = get_todos(filepath="todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = (f"{index + 1}-{item}")
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos(filepath="todos.txt")

            new_todo = input("enter the new todo")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos_arg=todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos(filepath="todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n') #Strip it so it doesn't Indent on print message
            todos.pop(index)

            write_todos("todos.txt", todos_arg=todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue


    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")

print("bye")
