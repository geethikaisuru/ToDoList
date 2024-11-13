import FreeSimpleGUI as sg
from zip import make_zip

label1 = sg.Text("Select files to compress")
input1 = sg.InputText(tooltip = "Select files you want to compress")
choose_button1 = sg.FilesBrowse("Choose", tooltip = "Select files to compress", key = "files")

label2 = sg.Text("Select where to compress")
input2 = sg.InputText(tooltip = "Select where you want to folder")
choose_button2 = sg.FolderBrowse("Choose", tooltip = "Select Destination compress", key = "folder")

compress_button = sg.Button("Compress", tooltip = "Compress the selected files")
output_label = sg.Text(key = 'output')

window = sg.Window('File Compresser', layout = [[ label1, input1, choose_button1],
                                                [ label2, input2, choose_button2], 
                                                [compress_button, output_label]])      

while True:
    event, values = window.read()
    print(values)
    print("That was Values\n")
    what = values['files'].split(";")
    where = values['folder']
    match event:
        case "Compress":
            make_zip(what, where)
            window["output"].update(value = "Compression Completed.")
        case sg.WIN_CLOSED:
            break

window.close()
