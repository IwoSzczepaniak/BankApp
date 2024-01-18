from Windows.common_tk_classes import *

class WindowInputTransfer(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            sender_id = sender_id_block.get()
            receiver_id = receiver_id_block.get()
            amount = amount_block.get()
            
            if len(sender_id) > 0 and len(receiver_id) and len(amount) > 0:
                text = f"INSERT INTO przelew (nr_konta_nadawcy, nr_konta_odbiorcy, kwota) VALUES ({sender_id[1:-2]}, {receiver_id[1:-2]}, {amount})"
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()
            sleep(0.01)

        # data
        sender_id_block = create_option_menu(self.window, "Nadawca", "Wybierz", get_select("SELECT nr_konta FROM konto"), 10)
        receiver_id_block = create_option_menu(self.window, "Odbiorca", "Wybierz", get_select("SELECT nr_konta FROM konto"), 10)
        amount_block = create_label_and_block(self.window, "Kwota", 10)
        

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        

        self.window.mainloop()
