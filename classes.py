import tkinter as tk
from db_functions import *

db_name="korki.db"
window_size = "500x600"

class Window:
    def __init__(self, title) -> None:
        self.window = tk.Tk()
        self.window_size = window_size
        self.window.title(title)
        self.window.geometry(self.window_size)

# extends Window
class WindowStart(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)

    def win_ic_close(self):
        self.window.destroy()
        windowInputClients = WindowInputClients("Wprowadź nowego klienta")
        windowInputClients.vis()


    def win_input_lessons_start(self):
        self.window.destroy()
        windowInputLessons = WindowInputLessons("Wprowadź nową lekcję")
        windowInputLessons.vis()

    def vis(self):
        clients_label = tk.Label(self.window, text="Dodaj nowego klienta i zobacz ich podgląd:")
        clients_label.pack()

        add_clients_button = tk.Button(self.window, text="Nowy klient", command=self.win_ic_close)
        add_clients_button.pack()

        lessons_label = tk.Label(self.window, text="\nDodaj nową lekcję:")
        lessons_label.pack()

        add_lessons_button = tk.Button(self.window, text="Nowa lekcja", command=self.win_input_lessons_start)
        add_lessons_button.pack()


        self.window.mainloop()

