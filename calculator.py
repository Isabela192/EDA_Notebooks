import PySimpleGUI as sg


sg.theme('Dark Brown')

# STEP 1 define the layout
layout = [ 
            [sg.Text('Enter the first number:', size=(15, 1)), sg.InputText()],
            [sg.Text('Enter the second number:', size=(15, 1)), sg.InputText()],
            [sg.Text('Choose an operation:', size=(15, 1)), sg.InputCombo(['+', '-', '*', '/'], size=(5, 1))],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
            [sg.Button('6'), sg.Button('5'), sg.Button('4'), sg.Button('*')],
            [sg.Button('3'), sg.Button('2'), sg.Button('1'), sg.Button('-')],
            [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
         ]

#STEP 2 - create the window
window = sg.Window('Calculator', layout, auto_size_buttons=False, default_element_size=(12,3), element_justification='center')

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Button':
      print('You pressed the button')
window.close()