from os import system
import json
import PySimpleGUI as sg
import discum
import sys

with open('settings.json') as f:
    d = json.load(f)
    token = str(d["token"])
    channelid = str(d["channelid"])


bot = discum.Client(token=token, log=False)
channel = channelid
system('cls')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')

def customsong():
    custom = [[sg.Text('Enter Song URL / Name:')],
              [sg.Input('', enable_events=True,  key='-INPUT-', )],
              [sg.Button('Ok', key='-OK-'), sg.Button('Exit')],
              [sg.Button('Submit', visible=False, bind_return_key=True)]]

    window = sg.Window('DEsH Custom Song', custom)

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == 'Submit':
            bot.sendMessage(str(channel), ';play ' + window['-INPUT-'].get())
            break

    window.close()

maingui = [[sg.Text("MAIN GUI")],
           [sg.Button("Pause"), sg.Button("UnPause")],
           [sg.Button("Leave")],
           [sg.Button("Loop")],
           [sg.Button("Lyrics")],
           [sg.Text("Queue GUI")],
           [sg.Button("Show Queue")],
           [sg.Button("Skip")],
           [sg.Button("Remove 1st From Queue")],
           [sg.Text("")]]

playgui = [[sg.Text("QuickPlay")],
           [sg.Button("Kwite - Backrooms")],
           [sg.Button("ANSI.sys")],
           [sg.Button("IMMA SHIT MY PANTS")],
           [sg.Button("Better Call Saul")],
           [sg.Button("Never Gonna Give You Up")],
           [sg.Button("XenoGenesis")],
           [sg.Button("Wenamachiindasama")],
           [sg.Button("Custom song")],
           [sg.Text("            By Xemulated")]]

layout = [[sg.VSeperator(),
           sg.Column(maingui),
           sg.VSeperator(),
           sg.Column(playgui),
           sg.VSeperator()]]

window = sg.Window("DEsH", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        exit()

    elif event == "Skip":
        bot.sendMessage(str(channel), ';skip')

    elif event == "Loop":
        bot.sendMessage(str(channel), ';loop')
    
    elif event == "Lyrics":
        bot.sendMessage(str(channel), ';lyrics')

    elif event == "Pause":
        bot.sendMessage(str(channel), ';pause')

    elif event == "UnPause":
        bot.sendMessage(str(channel), ';play')

    elif event == "Leave":
        bot.sendMessage(str(channel), ';leave')

    elif event == "Show Queue":
        bot.sendMessage(str(channel), ';q')

    elif event == "Kwite - Backrooms":
        bot.sendMessage(str(channel), ';play Kwite - the backrooms')

    elif event == "ANSI.sys":
        bot.sendMessage(str(channel), ';play Master Boot Record - ANSI.SYS')

    elif event == "IMMA SHIT MY PANTS":
        bot.sendMessage(str(channel), ';play Binky the Slinky - IMMA SHIT MY PANTS')

    elif event == "Better Call Saul":
        bot.sendMessage(str(channel), ';play Better Call Saul')

    elif event == "Never Gonna Give You Up":
        bot.sendMessage(str(channel), ';play Rick Astley - Never Gonna Give You Up')

    elif event == "XenoGenesis":
        bot.sendMessage(str(channel), ';play TheFatRat - Xenogenesis')

    elif event == "Wenamachiindasama":
        bot.sendMessage(str(channel), ';play Calvin Harris - Summer')

    elif event == "Custom song":
        customsong()

    elif event == "Skip":
        bot.sendMessage(str(channel), ';skip')

    elif event == "Remove 1st From Queue":
        bot.sendMessage(str(channel), ';remove 1')
