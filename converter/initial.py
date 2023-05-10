# Tutorials are from here https://www.youtube.com/watch?v=kQ8DGP9p2LY

import PySimpleGUI as sg

# sg.Window(title, layout)
layout = [
    [sg.Text('Text')],
    [sg.Button('Button')],
    [sg.Input()]
]

sg.Window('Converter', layout).read()
