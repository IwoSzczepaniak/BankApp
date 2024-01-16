from Windows.common_tk_classes import *
from Windows.db_functions import *

class WindowInputClients(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
    def vis(self):

        def update_client_preview():
            client_preview.delete(1.0, tk.END)  # Clear the text widget
            clients = get_select("SELECT * FROM klient;")

            if clients:
                for client in clients:
                    client_preview.insert(tk.END, f"ID: {client[0]},\tImię: {client[1]},\tNazwisko: {client[2]},\tPESEL:{client[3]},\tIlość mieszkań:{client[4]},\tOddział:{client[5]}\n")
            else:
                client_preview.insert(tk.END, "Brak klientów w bazie.")

        def save_name():
            name = name_block.get()
            surname = surname_block.get()
            pesel = pesel_block.get()
            realestate = realestate_block.get()
            branch = branch_block.get()

            if len(name) > 0 and len(surname) > 0 and len(pesel) > 0 and len(realestate)>0 and len(branch)>0:
                text = f"INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('{name}', '{surname}', '{pesel}', {realestate}, {branch});"
                error = execute_sql_query(text)
                # TODO error handling


            sleep(0.01)
            update_client_preview()

        def reset_clients():
            error = execute_sql_query("DELETE from klient")
            # TODO error handling
            update_client_preview()

        # data
        name_block = create_label_and_block(self.window, "Imię klienta", 10)
        surname_block = create_label_and_block(self.window, "Nazwisko klienta", 10)
        pesel_block = create_label_and_block(self.window, "PESEL klienta", 10)
        realestate_block = create_option_menu(self.window, "Czy posiada mieszkanie", "Wybierz", ['true', 'false'])
        branch_block = create_option_menu(self.window, "ID oddziału", "Wybierz", get_select("SELECT oddzial_id FROM oddzial_banku;"))
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

