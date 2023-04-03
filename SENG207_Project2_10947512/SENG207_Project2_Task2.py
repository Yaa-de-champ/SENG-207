
import PySimpleGUI as sg
import qrcode

sg.theme('DarkAmber')

layout = [[sg.InputText(key='url')],
            [sg.Button('Create', key='CREATE_BUTTON')],
            [sg.Image(key='image')]
]


window = sg.Window('QR Code Generator ', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'CREATE_BUTTON':
        url = values['url'] 

        img = qrcode.QRCode(version=1, box_size=10, border=5)
        img.add_data(url)
        img.make(fit=True)
        image = img.make_image(fill_color='black', back_color='white')

        image.save('qrcode.png')
        window['image'].update(filename='qrcode.png')



window.close()