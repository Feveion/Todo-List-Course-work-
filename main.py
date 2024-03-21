while True:
    user_action = input("type add, show, edit or exit")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)


            for index, item in enumerate(new_todos):
                row = (f"{index + 1}-{item}")
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit"))
            number = number - 1
            new_todo = input("enter the new todo")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo to complete"))
            todos.pop(number - 1)

        case 'exit':
            break

print("bye")
