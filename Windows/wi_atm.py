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
                # TODO error handling
            sleep(0.01)

        # data
        branch_id_block = create_option_menu(self.window, "ID oddziału do którego dodajesz bankomat", "Wybierz", get_select("SELECT oddzial_id from oddzial_banku"), 5)
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        self.window.mainloop()
