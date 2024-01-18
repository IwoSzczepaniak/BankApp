from Windows.common_tk_classes import *

class WindowInputTransaction(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            bankomat_id = bankomat_id_block.get()
            card_nr = card_nr_block.get()
            amount = amount_block.get()
            
            if len(bankomat_id) > 0 and len(card_nr) > 0 and len(amount) > 0:
                text = f"INSERT INTO transakcja (bankomat_id,  nr_karty, wplata_wyplata) VALUES ({bankomat_id[1:-2]}, {card_nr[1:-2]}, {amount});"
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()
            sleep(0.01)
        
        # data
        bankomat_id_block = create_option_menu(self.window, "ID bankomatu", "Wybierz", get_select("SELECT bankomat_id from bankomat"), 10)
        card_nr_block = create_option_menu(self.window, "Numer karty", "Wybierz", get_select("SELECT nr_karty from karta"), 10)
        amount_block = create_label_and_block(self.window, "Kwota", 10)
         

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        

        self.window.mainloop()
