#!/usr/bin/python3

"""
# styles (for white text only)

 1  = bold
 4  = underline
 5  = blink
 7  = highlighted (green)
 8  = light blank
 21 = double underline
 30 = dark blank
 31 = red
 32 = dark green
 33 = yellow
 34 = dark green
 35 = dark blue
 36 = blue
 37 = grey
*38 = white
 41 = bg red
 42 = bg green
 43 = bg yellow
 44 = bg green
 45 = bg dark blue
 46 = bg blue
 47 = bg grey
*48 = bg white
 53 = overline
 58 = bright

"""

data = {
        'bookmark' : 'intro',
        'menu' : 'intro',
        'text_speed' : 0.06,
        'wrap' : 32,
        'r' : 255,
        'g' : 255,
        'b' : 255
        }

color = {
        'white' : {'r' : 255, 'g' : 255, 'b' : 255},
        'grey' : {'r' : 128, 'g' : 128, 'b' : 128},
        'brown' : {'r' : 128, 'g' : 64, 'b' : 32},
        'yellow' : {'r' : 255, 'g' : 255, 'b' : 0},
        'green' : {'r' : 0, 'g' : 128, 'b' : 0},
        'blue' : {'r' : 0, 'g' : 0, 'b' : 255},
        'purple' : {'r' : 128, 'g' : 0, 'b' : 128},
        'red' : {'r' : 255, 'g' : 0, 'b' : 0},
        'orange' : {'r' : 255, 'g' : 128, 'b' : 0}
        }

menu = {# Technical
        'intro' : { # Intro
            'prompt' : 'Title',
            'style' : 38,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : '1-1', 'prompt' : 'New Game'},
                '2' : {'cmd' : '2', 'menu' : 'bookmark', 'prompt' : 'Continue'},
                '3' : {'cmd' : '3', 'menu' : 'settings', 'prompt' : 'Settings'},
                }},
        'settings' : { # Settings
            'prompt' : 'Settings',
            'style' : 38,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : 'speed_settings', 'prompt' : 'Text Speed'},
                '0' : {'cmd' : '0', 'menu' : 'bookmark', 'prompt' : 'Done'}
                }},
        'speed_settings' : { # Speed Settings
            'prompt' : 'Text Speed Settings',
            'style' : 38,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : 'settings', 'prompt' : 'Slowest'},
                '2' : {'cmd' : '2', 'menu' : 'settings', 'prompt' : 'Slow'},
                '3' : {'cmd' : '3', 'menu' : 'settings', 'prompt' : 'Normal'},
                '4' : {'cmd' : '4', 'menu' : 'settings', 'prompt' : 'Fast'},
                '5' : {'cmd' : '5', 'menu' : 'settings', 'prompt' : 'Fastest'}
                }},
        # Story
        '1-1' : { # 
            'prompt' : '',
            'style' : 38,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : '1-1', 'prompt' : ''},
                '2' : {'cmd' : '2', 'menu' : '1-1', 'prompt' : ''},
                '3' : {'cmd' : '3', 'menu' : '1-1', 'prompt' : ''},
                '4' : {'cmd' : '4', 'menu' : '1-1', 'prompt' : ''},
                '5' : {'cmd' : '5', 'menu' : '1-1', 'prompt' : ''},
                '6' : {'cmd' : '6', 'menu' : '1-1', 'prompt' : ''},
                '7' : {'cmd' : '7', 'menu' : '1-1', 'prompt' : ''},
                '8' : {'cmd' : '8', 'menu' : '1-1', 'prompt' : ''},
                '9' : {'cmd' : '9', 'menu' : '1-1', 'prompt' : ''},
                'x' : {'cmd' : 'x', 'menu' : '1-1', 'prompt' : 'Quit'}
                }},
        }
