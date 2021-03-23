import wolframalpha 
client = wolframalpha.Client("32HAHT-WTPJ5U7G8A")

import wikipedia

import PySimpleGUI as sg 



sg.theme('LightBlue')
layout = [[sg.Text('Enter command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]


window = sg.Window('Fragz', layout)

while True: 
    event, values = window.read()
    if event in (None, 'cancel'):
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences=2)

    import pyttsx3
    engine = pyttsx3.init()
    engine.say(wolfram_res)
    engine.say(wiki_res)
    sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia result: "+wiki_res)
    engine.runAndWait()


    print (values[0])

window.close()
