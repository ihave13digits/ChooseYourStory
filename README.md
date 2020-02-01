# ChooseYourStory

A template for a prompt and response game

This is a dictionary-driven engine, the dictionary is in var.py and the end is modified.
The stock scene naming is generic, and key to transitioning between scenes,
i.e. '1-1' would lead to '2-1', whereas '1-2' would lead to '2-2'.

Each scene will require:
    'prompt' (str) - a prompt to be displayed to the user in a set style
    'style' (int) - the style of text for the prompt
    'command' (dict) - a dictionary of user commands

Each 'command' will require:
    'cmd' (str) - user input to trigger command
    'menu' (str) - the scene to be next displayed
    'prompt' (str) -  the text displayed to the user
