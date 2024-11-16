import FreeSimpleGUI as sg
import zipfile

label1 = sg.Text("Select the Archive to Extract")
input1 = sg.Input(key = 'archive')
button1 = sg.FileBrowse("Browse", key= 'archive')

label2 = sg.Text("Select a folder to extract to")
input2 = sg.Input(key = 'folder')
button2 = sg.FolderBrowse("Browse", key= 'folder')

extract_button = sg.Button("Extract", key = 'extract')

window = sg.Window('Zip Extractor', 
        layout=[[label1, input1, button1],
                [label2, input2, button2],
                [extract_button]])
 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'extract':
        try:
            with zipfile.ZipFile(values['archive'], 'r') as zip_ref:
                zip_ref.extractall(values['folder'])
            sg.popup('Extraction Complete')
        except FileNotFoundError:
            sg.popup('File/Folder not found')
window.close()