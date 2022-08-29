from sys import exit
import sys
from os import system
import discum
import argparse

with open("token.txt") as mytxt:    # parses the token from and external file
    for line in mytxt:
        bot = discum.Client(token=line, log=False)

parser = argparse.ArgumentParser(description='')    # Parse arguments
parser.add_argument("--todo", type=str, default="NeverGonnaGiveYouUp")
args = parser.parse_args()
todov = args.todo

def start():    # loops over every possible argument
    channel = "CHANNELID"
    if todov == 'KwiteBackrooms':
        bot.sendMessage(channel, ';play kwite - the backrooms')
    elif todov == 'AnsiSys':
        bot.sendMessage(channel, ';play ANSI.SYS')
    elif todov == 'IMMASHITMYPANTS':
        bot.sendMessage(channel, ';play Binky the Slinky - IMMA SHIT MY PANTS')
    elif todov == 'BetterCallSaul':
        bot.sendMessage(channel, ';play Better Call Saul')
    elif todov == 'NeverGonnaGiveYouUp':
        bot.sendMessage(channel, ';play Never Gonna Give You Up')
    elif todov == 'Custom':
        with open('temp.txt') as f:
            songname = f.readlines()
        songname2 = str(songname).replace("['", "")
        songname = songname2.replace("']", "")
        bot.sendMessage(channel, ';play ' + str(songname))
    elif todov == 'Skip':
        bot.sendMessage(channel, ';skip')
    elif todov == 'Queue':
        bot.sendMessage(channel, ';q')
    else:
        exit()
    system('cls')
    exit()

start()