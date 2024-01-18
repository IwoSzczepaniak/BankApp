from Windows.common_tk_classes import *

class WindowInputAccount(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            client_id = client_id_block.get()
            saldo = saldo_block.get()
            
            if len(client_id) > 0 and len(saldo) > 0:
                text = f'INSERT INTO konto (klient_id, saldo) VALUES ({client_id[1:-2]}, {saldo})'
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()
            sleep(0.01)

        # data
        client_id_block = create_option_menu(self.window, "ID klienta", "Wybierz", get_select("SELECT klient_id FROM klient"), 10)
        saldo_block = create_label_and_block(self.window, "Saldo", 10)
    

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
    

        self.window.mainloop()
