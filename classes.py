import tkinter as tk
from db_functions import *
from time import sleep

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

class Window:
    def __init__(self, title) -> None:
        self.window = tk.Tk()
        self.window_size = "900x900"
        self.window.title(title)
        self.window.geometry(self.window_size)
        self.db_name = "bank.db"


class WindowStart(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)

    def win_ic_close(self, WindowClass, title):
        self.window.destroy()
        windowInputClients = WindowClass(title)
        windowInputClients.vis()

    def vis(self):
        create_label_and_button(self.window, "Dodaj nowego klienta i zobacz ich podgląd", "Nowy klient", lambda: self.win_ic_close(WindowInputClients, "Wprowadź nowego klienta"))
        create_label_and_button(self.window, "Dodaj nowy kredyt", "Nowy kredyt", lambda: self.win_ic_close(WindowInputCredit, "Wprowadź nowy kredyt"))

        self.window.mainloop()


class WindowInputClients(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
    def vis(self):

        def update_client_preview():
            client_preview.delete(1.0, tk.END)  # Clear the text widget
            clients = get_select(self.db_name, "SELECT * FROM klient;")

            if clients:
                for client in clients:
                    client_preview.insert(tk.END, f"ID: {client[0]},\tImię: {client[1]},\tNazwisko: {client[2]},\tPESEL:{client[3]},\tIlość mieszkań:{client[4]},\tOddział:{client[5]}\n")
            else:
                client_preview.insert(tk.END, "Brak klientów w bazie.")
            
            # client_preview.tag_configure("center", justify="center")
            # client_preview.tag_add("center", "1.0", "end")


        def save_name():
            name = name_block.get()
            surname = surname_block.get()
            pesel = pesel_block.get()
            realestate = realestate_block.get()
            branch = branch_block.get()

            if len(name) > 0 and len(surname) > 0 and len(pesel) > 0 and len(realestate)>0 and len(branch)>0:
                text = f"INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('{name}', '{surname}', '{pesel}', {realestate}, {branch});"
                execute_sql_querry(self.db_name, text)

            sleep(0.01)
            update_client_preview()

        def reset_clients():
            execute_sql_querry(self.db_name, "DELETE from klient")
            update_client_preview()

        # data
        name_block = create_label_and_block(self.window, "Imię klienta", 10)
        surname_block = create_label_and_block(self.window, "Nazwisko klienta", 10)
        pesel_block = create_label_and_block(self.window, "PESEL klienta", 10)
        realestate_block = create_label_and_block(self.window, "Ilość mieszkań", 10)
        branch_block = create_label_and_block(self.window, "Najbliższy oddział", 10)
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        # preview
        client_preview = tk.Text(self.window, height=15, width=100)
        client_preview.pack(pady=10)
        update_client_preview()
        # 

        # reset db
        reset_button = tk.Button(self.window, text="Resetuj bazę danych", command=reset_clients)
        reset_button.pack(pady=10)
        # 

        self.window.mainloop()



class WindowInputCredit(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            client_id = client_id_block.get()
            credit_type = credit_type_block.get()
            amount = amount_block.get()

            if len(client_id) > 0 and len(credit_type) > 0 and len(amount) > 0:
                # text = f"INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('{name}', '{surname}', '{pesel}', {realestate}, {branch});"
                # TODO
                text = ''
                execute_sql_querry(self.db_name, text)

            sleep(0.01)

        # data
        client_id_block = create_label_and_block(self.window, "Numer klienta", 10)
        credit_type_block = create_label_and_block(self.window, "Typ kredytu", 10)
        amount_block = create_label_and_block(self.window, "Kwota kredytu", 10)
        
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        self.window.mainloop()