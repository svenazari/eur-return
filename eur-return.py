#EURreturn
#potrebni programi: Python3, PySimpleGUI
#by: SvenAzari
#https://github.com/svenazari

import PySimpleGUI as sg

sg.theme ("DarkGrey5") #tema

layout = [  [sg.Text("Iznos"), sg.InputText(size=(6,1), key='izn')],
            [sg.Button("EUR to HRK")], 
            [sg.Button("HRK to EUR")],
            [sg.Text("", text_color='yellow', key='izncon')],
            [sg.Text("Cijena EUR"), sg.InputText(size=(6,1), key='eur')], #unos cijene u eurima
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
        window['izn'].update('')
        window['izncon'].update('')
    elif event == "EUR to HRK":
        hrk = values['izn'] #iznso u hrk
        if hrk == "":
            pass
        else:
            hrkf = float(hrk.replace(',','.')) #float hrk
            eur = round(hrkf * 7.53450,2)
            eurp = str(eur) + " HRK"
            window['izncon'].update(eurp)
    elif event == "HRK to EUR":
        eur = values['izn'] #cijena u eur
        if eur == "":
            pass
        else:
            eurf = float(eur.replace(',','.')) #float eur
            kn = round(eurf / 7.53450,2)
            knp = str(kn) + " EUR"
            window['izncon'].update(knp)
    elif event == "IZRAČUNAJ":
        eur = values['eur'] #cijena
        if eur == "":
            pass
        else:
            eurf = float(eur.replace(',','.')) #float eur
            hrk = values['hrk'] #plaćeni iznos
            hrkf = float(hrk.replace(',','.')) #float hrk
            rate = 7.53450 #fiksni tečaj za konverziju
        #računanje
            hrk2eur = round(hrkf / rate,2) #pretvaranje kuna u euro
            raz = round(hrk2eur - eurf,2) #računanje razlike
            razp = "Za vratiti " + str(raz) + " EUR"
            window['back'].update(razp)

#verzija 3: preračunavanje iz kuna u euro i obratno u gornjem dijelu prozora
#verzija 2: dodana mogućnost da se cijena u EUR preračuna u HRK
#verzija 1: osnovno preračunavanje i izračuna razlike u eurima
