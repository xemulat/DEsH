from os import system
from time import sleep
from json import load
import PySimpleGUI as sg
import discum
import sys

def sand(send):
    bot.sendMessage(str(channel), send)
    sleep(1)

with open('settings.json') as f:
    d = load(f)
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
            sand(';play ' + window['-INPUT-'].get())
            break

    window.close()

maingui = [[sg.Text("MAIN GUI")],
           [sg.Button("Pause"), sg.Button("UnPause")],
           [sg.Button("Leave")],
           [sg.Button("Loop")],
           [sg.Button("Lyrics")],
           [sg.Text("Queue GUI")],
           [sg.Button("Show Queue"), sg.Button("Skip")],
           [sg.Button("Remove 1st From Queue")],
           [sg.Text("")],
           [sg.Text("DEsH v2.1")],
           [sg.Text("CopyLeft Xemulated 2022")]]

playgui = [[sg.Text("QuickPlay")],
           [sg.Button("Kwite - Backrooms")],
           [sg.Button("ANSI.sys")],
           [sg.Button("IMMA SHIT MY PANTS")],
           [sg.Button("Better Call Saul")],
           [sg.Button("Never Gonna Give You Up")],
           [sg.Button("XenoGenesis")],
           [sg.Button("Wenamachiindasama")],
           [sg.Button("Welcum to the cum zone")],
           [sg.Button("Custom song")],
           [sg.Text("")]]

layout = [[sg.VSeperator(),
           sg.Column(maingui),
           sg.VSeperator(),
           sg.Column(playgui),
           sg.VSeperator()]]

window = sg.Window("DEsH2", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        exit()

    elif event == "Skip":
        sand(';skip')

    elif event == "Loop":
        sand(';loop')

    elif event == "Lyrics":
        sand(';lyrics')

    elif event == "Pause":
        sand(';pause')

    elif event == "UnPause":
        sand(';play')

    elif event == "Leave":
        sand(';leave')

    elif event == "Show Queue":
        sand(';q')

    elif event == "Welcum to the cum zone":
        sand(';play Welcum to the cum zone')

    elif event == "Kwite - Backrooms":
        sand(';play Kwite - the backrooms')

    elif event == "ANSI.sys":
        sand(';play Master Boot Record - ANSI.SYS')

    elif event == "IMMA SHIT MY PANTS":
        sand(';play Binky the Slinky - IMMA SHIT MY PANTS')

    elif event == "Better Call Saul":
        sand(';play Better Call Saul')

    elif event == "Never Gonna Give You Up":
        sand(';play Rick Astley - Never Gonna Give You Up')

    elif event == "XenoGenesis":
        sand(';play TheFatRat - Xenogenesis')

    elif event == "Wenamachiindasama":
        sand(';play Calvin Harris - Summer')

    elif event == "Custom song":
        customsong()

    elif event == "Skip":
        sand(';skip')

    elif event == "Remove 1st From Queue":
        sand(';remove 1')
