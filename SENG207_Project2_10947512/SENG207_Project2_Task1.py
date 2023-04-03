
import PySimpleGUI as sg
import pyttsx3 

sg.theme('DarkAmber')


layout = [ 
                
            [sg.InputText(key='Inputed_Text'), sg.Button('Speak', key='SPEAK_BUTTON')],      
            [sg.Text('Select Voice Type'), sg.Radio('Male','VOICE',default=True, key='male'), sg.Radio('Female', 'VOICE', key='female')],
]

window = sg.Window('Text to Speech App', layout)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'SPEAK_BUTTON':        
        text = values['Inputed_Text']
        
        if values['male']:
            engine.setProperty('voice', voices[0].id)
        elif values['female']:
            engine.setProperty('voice', voices[1].id)
            
        engine.say(text)
        engine.runAndWait()

window.close()

