import PySimpleGUI as sg

import windows2
import windows3
import windows4

layout = [
    [sg.Text('Выберите задачу')],
    [sg.Button('Задача 2'), sg.Button('Задача 3'), sg.Button('Задача 4')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File Compare', layout)

while True:                     # The Event Loop
    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = isitago = None
        print(values)

    if event == 'Задача 2':
        windows2.make_win2();

    if event == 'Задача 3':
        windows3.make_win3();

    if event == 'Задача 4':
        windows4.make_win4();

      


window.close()