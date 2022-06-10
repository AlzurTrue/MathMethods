import PySimpleGUI as sg
import functions

def make_win2():
    layout = [[sg.Text('Задача 2')],
              [sg.Text('Ввод новых значений здесь пока не работает')],
              [sg.Text("a           b           c           d           k           l           m           n")],
              [sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None)), sg.Input(size=(5, None))],
              [sg.Output(size=(88, 20))],
              [sg.Submit(), sg.Cancel()]]
    window = sg.Window('Window Title', layout)

    while True:  # The Event Loop
        event, values = window.read()
        print(event, values) #debug
        if event == 'Submit':
            o = functions.Optimization()
            o.start(2)


        if event in (None, 'Exit', 'Cancel'):
            window.close();
            break