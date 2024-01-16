import tkinter as tk
from Windows.db_functions import *
from time import sleep

class Window:
    def __init__(self, title) -> None:
        self.window = tk.Tk()
        self.window_size = "900x900"
        self.window.title(title)
        self.window.geometry(self.window_size)
        self.db_name = "bank.db"

def create_label_and_block(win, label_text:str, pad_y:int = 5):
    label = tk.Label(win, text=label_text)
    label.pack(pady=pad_y)
    block = tk.Entry(win)
    block.pack(pady=pad_y)
    return block

def create_label_and_button(win, label_text:str, btn_txt:str, command, pad_y:int = 5):
    label = tk.Label(win, text=label_text)
    label.pack(pady=pad_y)
    button = tk.Button(win, text=btn_txt, command=command)
    button.pack(pady=pad_y)
    return button

def create_option_menu(win, label_text:str, list_text:str, options, pad_y:int = 5):
    select_label = tk.Label(win, text=label_text)
    select_label.pack(pady=pad_y)

    selected_client = tk.StringVar(win)
    selected_client.set(list_text) # set the default value to the first client in the list

    # create the option menu widget
    client_menu = tk.OptionMenu(win, selected_client, *options)
        
    client_menu.pack(pady=pad_y)

    return selected_client
