import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Type in a to-do", key="todoInput")
add_button = sg.Button("Add", tooltip="Add the typed to-do")
list_box = sg.Listbox(values = functions.get_todos(), key='todos',
                                enable_events = True ,size=(50, 10))
edit_button = sg.Button("Edit", tooltip="Edit the selected to-do")
complete_button = sg.Button("Complete", key="complete_button")
exit_button = sg.Button("Exit", tooltip="Exit the program")

window = sg.Window('My To-Do App' , 
                    layout=[[label, input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font=('Helvetica' , 18))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todoInput'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todoInput']
            
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todoInput'].update(value=values['todos'][0])
        case 'complete_button':
            todos = functions.get_todos()
            todos.remove(values['todos'][0])
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Exit':
            break  
        case sg.WIN_CLOSED:
            break

window.close()