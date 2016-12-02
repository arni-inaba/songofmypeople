# encoding=utf-8

import os
import sys
import json
import random

import pygame as pg


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


pg.init()
pg.mixer.init()
pg.mixer.set_num_channels(50)

sound_path = os.getenv('APP_LOC', '.')
full_pnotes_path = [
    'wav/bell_01.wav',
    'wav/bell_02.wav',
    'wav/bell_03.wav',
    'wav/bell_04.wav',
    'wav/bell_05.wav',
    'wav/bell_06.wav',
    'wav/bell_07.wav',
    'wav/bell_08.wav',
    'wav/bell_09.wav',
    'wav/bell_10.wav'
]

full_pnotes_path = ['{}/{}'.format(sound_path, p) for p in full_pnotes_path]
pnotes = [pg.mixer.Sound(p) for p in full_pnotes_path]

full_offnotes_path = [
    'wav/bell_11_off.wav',
    'wav/bell_12_off.wav'
]
full_offnotes_path = ['{}/{}'.format(sound_path, op) for op in full_offnotes_path]

offnotes = [pg.mixer.Sound(p) for p in full_offnotes_path]


def sing(status):
    if status < 300:
        note = random.choice(pnotes)
        print('\r{}{}{}'.format(BColors.OKGREEN, status, BColors.ENDC))
    else:
        note = random.choice(offnotes)
        print('\r{}{}{}'.format(BColors.FAIL, status, BColors.ENDC))
    note.play()


while True:
    line = sys.stdin.readline()
    try:
        logline = json.loads(line)
        status = int(logline['@fields']['status'])
        sing(status)
    except KeyboardInterrupt:
        sys.exit()
    except json.JSONDecodeError:
        pass
