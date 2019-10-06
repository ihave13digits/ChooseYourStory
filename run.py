#!/usr/bin/python3

import os, sys, time, textwrap

from var import *

running = True

clear_cmd = ''

if sys.platform.startswith('win32'):
    clear_cmd = 'cls'
else:
    clear_cmd = 'clear'

class Engine():

    def data(save, mode):
        with open(save, mode) as f:
            if mode == "w":
                for key in data:
                    f.write(str(data[key]))
                    f.write("\n")

            if mode == "r":
                data['bookmark'] = str(f.readline().strip())
                data['menu'] = str(f.readline().strip())
                data['text_speed'] = float(f.readline().strip())
                data['wrap'] = int(f.readline().strip())
                data['r'] = int(f.readline().strip())
                data['g'] = int(f.readline().strip())
                data['b'] = int(f.readline().strip())

    def menu(M, margin=3):
        #   Show Prompt
        global running, data
        wrapped_txt = str('\n'.join(textwrap.wrap(menu[data['menu']]['prompt'], data['wrap'], break_long_words=False)))
        for c in wrapped_txt:
            sys.stdout.write("\x1b[{};2;{};{};{}m".format(menu[data['menu']]['style'], data['r'], data['g'], data['b']) + c + '\x1b[0m')
            sys.stdout.flush()
            time.sleep(data['text_speed'])
        print("\n"* margin)
    
        #   Show Commands
        for m in menu[data['menu']]['command']:
            print("({}) {}".format(
                menu[data['menu']]['command'][m]['cmd'],
                menu[data['menu']]['command'][m]['prompt']))

        #   Get Special Commands
        sel = input(": ")
        os.system(clear_cmd)
        if sel == "main" or sel == "home":
            Engine.data('data.txt', 'w')
            data['menu'] = 'intro'
        if sel == "settings" or sel == "options":
            Engine.data('data.txt', 'w')
            data['menu'] = 'settings'
        if sel == "x":
            Engine.data("data.txt", "w")
            running = False
        try:
            if data['menu'] == "speed_settings":
                if sel == "1":
                    data['text_speed'] = 0.12
                if sel == "2":
                    data['text_speed'] = 0.09
                if sel == "3":
                    data['text_speed'] = 0.06
                if sel == "4":
                    data['text_speed'] = 0.03
                if sel == "5":
                    data['text_speed'] = 0.01
            # Loading
            if data['menu'] == "intro":
                if sel == "2":
                    data['menu'] = data['bookmark']
            # Jump Menus
            if menu[data['menu']]['command'][sel]['menu'] == "bookmark":
                data['menu'] = data['bookmark']
    
        #   Get Normal Command
            else:
                if menu[data['menu']]['command'][sel]['menu'] != "bookmark":
                    data['menu'] = menu[data['menu']]['command'][sel]['menu']
                if data['menu'] != "intro" and data['menu'] != "settings" and data['menu'] != "speed_settings":
                    data['bookmark'] = menu[data['menu']]['command'][sel]['menu']
        except KeyError:
            pass
        Engine.data("data.txt", "w")

    def update():
        Engine.data("data.txt", "r")
        Engine.menu(data['menu'])

    def start():
        try:
            os.system(clear_cmd)
            Engine.run()
        except FileNotFoundError:
            Engine.data("data.txt", "w")
            Engine.run()

    def run():
        while running:
            Engine.update()

Engine.start()
