from Windows.common_tk_classes import *

class WindowInputCard(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            account_id = account_id_block.get()
            card_type = card_type_block.get()
            
            if len(account_id) > 0 and len(card_type) > 0:
                text = f"INSERT INTO karta (nr_konta, rodzaj_karty) VALUES ({account_id[1:-2]}, '{card_type}')"
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()
            sleep(0.01)

        # data
        account_id_block = create_option_menu(self.window, "Numer konta", "Wybierz", get_select("SELECT nr_konta FROM konto"), 10)
        card_type_block = create_option_menu(self.window, "Rodzaj karty", "Wybierz", ["Credit", "Debit"], 10)
   

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
    

        self.window.mainloop()
