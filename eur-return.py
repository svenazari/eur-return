#EURreturn
#potrebni programi: Python3, PySimpleGUI
#by: SvenAzari
#https://github.com/svenazari

import PySimpleGUI as sg

sg.theme ("DarkGrey5") #tema

layout = [  [sg.Text("Cijena EUR"), sg.InputText(size=(6,1), key='eur')], #unos cijene u eurima
            [sg.Text("Plaćeno HRK"), sg.InputText(size=(6,1), key='hrk')], #unos plaćenog u kunama
            [sg.Text("Za vratiti", text_color='yellow', key='back')], #mjesto za ispis izračuna
            [sg.Button("IZRAČUNAJ")], 
            [sg.Button("NOVO")], 
            [sg.Button("EXIT")]
    ]

window = sg.Window("EUR RETURN", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    elif event == "NOVO":
        window['eur'].update('')
        window['hrk'].update('')
        window['back'].update('Za vratiti')
    elif event == "IZRAČUNAJ":
        eur = values['eur'] #cijena
        eurf = float(eur.replace(',','.')) #float eur
        hrk = values['hrk'] #plaćeni iznos
        hrkf = float(hrk.replace(',','.')) #float hrk
        rate = 7.53450 #fiksni tečaj za konverziju
        #računanje
        hrk2eur = round(hrkf / rate,2) #pretvaranje kuna u euro
        raz = round(hrk2eur - eurf,2) #računanje razlike
        razp = "Za vratiti " + str(raz) + " EUR"
        window['back'].update(razp)

#verzija 1: osnovno preračunavanje i izračuna razlike u eurima