from functions import get_todos, write_todos

while True:
    user_action = input("Please Enter an action(add, show, edit, complete): ").strip()

    if user_action.startswith("add"):
        todos = get_todos()
        todo = user_action[4:] + '\n'
        todos.append(todo)
        write_todos(todos,)
        print(todos)  

        
    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:            
            todos = get_todos()
            editNumber = (int(user_action[5:]) - 1)
            print("You want to edit item number: ", todos[editNumber])  
            todos[editNumber] = input("Enter a new todo:") + '\n'

            write_todos('todos.txt', todos)
            print("Todo edited successfully")

        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            
            write_todos(todos)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
         break

    else :
        print("Command not Valid")
