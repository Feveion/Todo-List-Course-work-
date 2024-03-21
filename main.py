while True:
    #Get user input and strip space chars from it.
    user_action = input("type add, show, edit or exit")
    user_action = user_action.strip()


    if 'add' in user_action :
        # [4:] is line splicing, cuts first 4 characters.4:8 have a range of saved chars saving 4 - 8
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = (f"{index + 1}-{item}")
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("enter the new todo")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n') #Strip it so it doesn't Indent on print message
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("command is not valid")

print("bye")
