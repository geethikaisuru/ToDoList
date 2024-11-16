import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as f:
        pass

# Create a GUI window
sg.theme('DarkAmber')
clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Type in a to-do", key="todoInput")
list_box = sg.Listbox(values = functions.get_todos(), key='todos',
                                enable_events = True ,size=(50, 10))
edit_button = sg.Button("Edit", tooltip="Edit the selected to-do")

add_button = sg.Button("Add", key = "Add", tooltip="Add the typed to-do")
complete_button = sg.Button("Complete", key="complete_button", tooltip="Complete the selected to-do")
exit_button = sg.Button("Exit", tooltip="Exit the program")

window = sg.Window('My To-Do App' , 
                    layout=[[clock],
                            [label, input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font=('Helvetica' , 18))

while True:
    event, values = window.read(timeout=500 )
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todoInput'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todoInput']
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('No to-do is selected. Please select a to-do to edit', font = ('Helvetica', 18))
                pass
        case 'todos':
            window['todoInput'].update(value=values['todos'][0])
        case 'complete_button':
            try:
                todos = functions.get_todos()
                todos.remove(values['todos'][0])
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('No to-do is selected', font = ('Helvetica', 18))
                pass
        case 'Exit':
            break  
        case sg.WIN_CLOSED:
            break

window.close()