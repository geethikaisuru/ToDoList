import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.InputText(tooltip = "Select files you want to compress")
choose_button1 = sg.FilesBrowse("Choose", tooltip = "Select files to compress")

label2 = sg.Text("Select the destination folder")
input2 = sg.InputText(tooltip = "Select the destination folder")
choose_button2 = sg.FolderBrowse("Choose", tooltip = "Select Destination compress")

compress_button = sg.Button("Compress", tooltip = "Compress the selected files")

window = sg.Window('File Compresser', layout = [[ label1, input1, choose_button1],[ label2, input2, choose_button2], [compress_button]])      
window.read()
window.close()    