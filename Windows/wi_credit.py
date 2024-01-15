from Windows.common_tk_classes import *

class WindowInputCredit(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            client_id = client_id_block.get()
            credit_type = credit_type_block.get()
            amount = amount_block.get()
            start_date = start_date_block.get()
            end_date = end_date_block.get()
            
            if len(client_id) > 0 and len(credit_type) > 0 and len(amount) > 0 and len(start_date)==10 and len(end_date)==10:
                text = f'INSERT INTO kredyt_detale (klient_id, typ_kredytu_id, kwota, data_zaciagniecia, data_splaty) VALUES ({client_id[1]}, "{credit_type[1]}", {amount}, "{start_date}", "{end_date}")'
                error = execute_sql_querry(text)
                if error:
                    # TODO error handling
                    pass
            sleep(0.01)

        # data
        client_id_block = create_option_menu(self.window, "ID klienta", "Wybierz klienta", get_select("SELECT klient_id FROM klient;"), 10)
        credit_type_block = create_option_menu(self.window, "Typ kredytu", "Wybierz typ kredytu", get_select("SELECT typ_kredytu_id FROM typ_kredytu;"), 10)
        amount_block = create_label_and_block(self.window, "Kwota kredytu", 10)
        start_date_block = create_label_and_block(self.window, "Data zaciągnięcia", 10)
        end_date_block = create_label_and_block(self.window, "Data spłaty", 10)
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        self.window.mainloop()
