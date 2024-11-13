from functions import convert_to_meters
import FreeSimpleGUI as sg

feet_label = sg.Text("Feet:", key="feets")
feet_input = sg.Input(key="feet_input")

inches_label = sg.Text("Inches:", key="inches")
inches_input = sg.Input(key="inches_input")

convert_button = sg.Button("Convert", key="convert_button")
output_label = sg.Text("Output:", key="output_label")

window = sg.Window("Feet & Inches Converter", 
        layout= [[feet_label, feet_input],
                [inches_label, inches_input],
                [convert_button, output_label]], 
                font=('Helvetica', 18))

while True:
    event, values = window.read()
    print(event, values)
    if event == "convert_button":
        try:
            feet = int(values["feet_input"])
            inches = int(values["inches_input"])
            output = convert_to_meters(feet, inches)
            window["output_label"].update(f"Converted to Meters: {output}")
        except ValueError:
            window["output_label"].update("Please enter valid numbers")
    if event == sg.WIN_CLOSED:
        break

window.close()