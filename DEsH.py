from os import system
from os.path import isfile
from time import sleep
from json import load
from urllib.request import urlretrieve
import PySimpleGUI as sg
import discum
import sys

if isfile("settings.json") == False:
    urlretrieve('https://github.com/xemulat/DEsH/releases/download/1.0/settings.json', 'settings.json')
    custo = [[sg.Text('ERROR 01: Fill out the new settings.json File.')],
             [sg.Button('Exit')]]
    window = sg.Window('DEsH Config Error', custo)
    while True:
        event, values = window.read()
        if event == 'Exit':
            exit()
elif isfile("settings.json") == True:
    with open('settings.json') as f:
        d = load(f)
        token = str(d["token"])
        channelid = str(d["channelid"])
        addon1 = str(d["activateaddon"])
        prefis = str(d["prefix"])

if addon1 == 'true':
    isaddon = " + BetterPlayer"
else:
    isaddon = " "
bot = discum.Client(token=token, log=False)
channel = channelid
system('cls')
sg.theme("DarkGray15")
sg.set_options(font=("Consolas", 9), text_color='#FFFFFF')

def sand(send):
    send = prefis + send
    bot.sendMessage(str(channel), send)
    sleep(1)

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
            sand('play ' + window['-INPUT-'].get())
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
           [sg.Text("DEsH v2.1" + isaddon)],
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
           [sg.Button("Imagine Dragons - Bones")],
           [sg.Button("Custom song")]]

if addon1 == 'true':
    addon1ui = [[sg.Text("VolumeControl")],
                [sg.Button("50%"), sg.Button("100%"), sg.Button("150%"), sg.Button("200%")],
                [sg.Text("")],
                [sg.Text("MoreSongs")],
                [sg.Button("Minecraft Soundtrack")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")],
                [sg.Text(" ")]]

if addon1 == 'true':
    layout = [[sg.VSeperator(),
               sg.Column(maingui),
               sg.VSeperator(),
               sg.Column(playgui),
               sg.Column(addon1ui),
               sg.VSeperator()]]
elif addon1 == 'false':
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

# ----------< MAIN GUI >----------

    elif event == "Loop":
        sand('loop')

    elif event == "Lyrics":
        sand('lyrics')

    elif event == "Pause":
        sand('pause')

    elif event == "UnPause":
        sand('play')

    elif event == "Leave":
        sand('leave')

# ----------< Queue >----------

    elif event == "Show Queue":
        sand('q')

    elif event == "Skip":
        sand('skip')

    elif event == "Remove 1st From Queue":
        sand('remove 1')

# ----------< QuickPlay >----------

    elif event == "Welcum to the cum zone":
        sand('play Welcum to the cum zone')

    elif event == "Kwite - Backrooms":
        sand('play Kwite - the backrooms')

    elif event == "ANSI.sys":
        sand('play Master Boot Record - ANSI.SYS')

    elif event == "IMMA SHIT MY PANTS":
        sand('play Binky the Slinky - IMMA SHIT MY PANTS')

    elif event == "Better Call Saul":
        sand('play Better Call Saul')

    elif event == "Never Gonna Give You Up":
        sand('play Rick Astley - Never Gonna Give You Up')

    elif event == "XenoGenesis":
        sand('play TheFatRat - Xenogenesis')

    elif event == "Wenamachiindasama":
        sand('play Calvin Harris - Summer')

    elif event == "Imagine Dragons - Bones":
        sand('play Imagine Dragons - Bones')

    elif event == "Custom song":
        customsong()

# ----------< BetterPlayer >----------
    if addon1 == 'true':
        if event == "50%":
            sand('volume 50')
        
        elif event == "100%":
            sand('volume 100')
        
        elif event == "150%":
            sand('volume 150')
        
        elif event == "200%":
            sand('volume 200')
        
        elif event == "Minecraft Soundtrack":
            sand('play https://open.spotify.com/playlist/3dmhlm4EI6HG7juCdN9fHc')
