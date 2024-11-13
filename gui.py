import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Type in a to-do", key="todoInput")
add_button = sg.Button("Add", tooltip="Add the typed to-do")

window = sg.Window('My To-Do App' , 
                    layout=[[label, input_box, add_button]], 
                    font=('Helvetica' , 18))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todoInput'] + '\n')
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()