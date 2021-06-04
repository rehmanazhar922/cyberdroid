import PySimpleGUI as g
import os

layout = [  [g.Text("target : ")], [g.Input(key='-Target-')],
            [g.Button('Ok')], 
            [g.Button("exit")],
            [g.Button('disconnect')]]

window = g.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == g.WINDOW_CLOSED or event == 'Quit' or event == 'exit' or event == 'disconnect':
        os.system("adb disconnect " + values['-Target-'] + ":5555")
        break
    os.system("adb connect " + values['-Target-'] + ":5555")
    os.system("scrcpy")
    os.system("adb disconnect " + values['-Target-'] + ":5555")

window.close() 