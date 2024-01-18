from Windows.common_tk_classes import *

class WindowInputATM(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def save_name():
            branch_id = branch_id_block.get()
            
            if len(branch_id) > 0: 
                text = f"INSERT INTO bankomat (oddzial_id) VALUES ({branch_id[1:-2]})"
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()
            sleep(0.01)
            update_atm_preview()

        def update_atm_preview():
            atm_preview.delete(1.0, tk.END)
            atms = get_select("SELECT * FROM bankomat;")
            if atms:
                for atm in atms:
                    atm_preview.insert(tk.END, f"ID: {atm[0]},\tOddział: {atm[1]}\n")
            else:
                atm_preview.insert(tk.END, "Brak bankomatów w bazie.")
            

        # data
        branch_id_block = create_option_menu(self.window, "ID oddziału do którego dodajesz bankomat", "Wybierz", get_select("SELECT oddzial_id from oddzial_banku"), 5)
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        atm_preview = tk.Text(self.window, height=12, width=80)
        atm_preview.pack(pady=10)
        update_atm_preview()

        self.window.mainloop()
