from os import system
import sys
import base58
import PySimpleGUI as sg
# i wanna fucking de-alive myself bruh

sp = "                                      "

def starter(todo):
    return "python DEsH-Server.py --todo " + todo + " && cls"


system('cls')

def playgui():
    layout = [[sg.Text("What to play? (app will freeze for ~5s)  ")],
             [sg.Button("Kwite - Backrooms")],
             [sg.Button("ANSI.sys")],
             [sg.Button("IMMA SHIT MY PANTS")],
             [sg.Button("Better Call Saul")],
             [sg.Button("Never Gonna Give You Up")],
             [sg.Button("Custom song (look at the console)")],
             [sg.Button("Back")]]

    window = sg.Window("DEsH SongClient", layout, background_color='#000000')

    while True:
        event, values = window.read()
        if event == "Kwite - Backrooms":
            system(starter("KwiteBackrooms"))
        if event == "ANSI.sys":
            system(starter("AnsiSys"))
        if event == "IMMA SHIT MY PANTS":
            system(starter("IMMASHITMYPANTS"))
        if event == "Better Call Saul":
            system(starter("BetterCallSaul"))
        if event == "Never Gonna Give You Up":
            system(starter("NeverGonnaGiveYouUp"))
        if event == "Custom song (look at the console)":
            songname = input("INPUT THE SONG'S NAME: ")
            with open('temp.txt', 'w') as f:
                f.write(songname)
            system(starter("Custom"))
        if event == sg.WIN_CLOSED or event == "Back":
            break

    window.close()


def maingui():
    layout = [[sg.Text("What to do?" + sp)],
              [sg.Button("Play Something")],
              [sg.Button("Show Queue")],
              [sg.Button("Skip")],
              [sg.Button("Exit")]]
    window = sg.Window("DEsH Client", layout, background_color='#000000')

    while True:
        event, values = window.read()
        if event == "Play Something":
            playgui()
        if event == "Skip":
            system(starter("Skip"))
        if event == "Show Queue":
            system(starter("Queue"))
        if event == sg.WIN_CLOSED or event == "Exit":
            break

    window.close()

maingui()