from Windows.common_tk_classes import *

class WindowInputBranch(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
        
    def vis(self):

        def update_branch_preview(): 
            branch_preview.delete(1.0, tk.END)  # Clear the text widget
            branches = get_select("SELECT * FROM oddzial_banku;")

            if branches:
                for branch in branches:
                    branch_preview.insert(tk.END, f"ID: {branch[0]},\tAdres: {branch[1]}\n")
            else:
                branch_preview.insert(tk.END, "Brak adresów w bazie.")
            


        def save_name():
            address = address_block.get()
            
            if len(address) > 0:
                text = f"INSERT INTO oddzial_banku (adres) VALUES ('{address}')"
                error = execute_sql_query(text)
                # TODO error handling
            sleep(0.01)
            update_branch_preview()

        # data
        address_block = create_label_and_block(self.window, "Adres", 10)
        # 
        
        # preview
        branch_preview = tk.Text(self.window, height=15, width=100)
        branch_preview.pack(pady=15)
        update_branch_preview()
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=15)
        # 

        self.window.mainloop()
