from Windows.common_tk_classes import *
from Windows.db_functions import *

class WindowInputCreditType(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)
    def vis(self):

        def update_credit_preview():
            credit_preview.delete(1.0, tk.END)  # Clear the text widget
            credit_types = get_select("SELECT * FROM typ_kredytu;")

            if credit_types:
                for credit_type in credit_types:
                    credit_preview.insert(tk.END, f"ID: {credit_type[0]},\tOprocentowanie: {credit_type[1]},\tMaks. kwota: {credit_type[2]},\tPula całkowita:{credit_type[3]},\tAktualna pula:{credit_type[4]},\tOddział:{credit_type[5]}\n")
            else:
                credit_preview.insert(tk.END, "Brak klientów w bazie.")

        def save_name():
            procent = procent_block.get()
            max_amount = max_amount_block.get()
            total_pool = total_pool_block.get()
            current_pool = current_pool_block.get()            
            branch = branch_block.get()

            if len(procent) > 0 and len(max_amount) > 0 and len(total_pool) > 0 and len(current_pool)>0 and len(branch)>0:
                text = f"INSERT INTO typ_kredytu (oprocentowanie, maksymalna_kwota, pula_srodkow, aktualna_pula_srodkow, oddzial_id) VALUES ({procent}, {max_amount}, {total_pool}, {current_pool}, {branch[1:-2]});"
                error = execute_sql_query(text)
                if error:
                    error_window = WindowError("Błąd", error)
                    error_window.vis()


            sleep(0.01)
            update_credit_preview()


        # data
        procent_block = create_label_and_block(self.window, "Oprocentowanie", 10)
        max_amount_block = create_label_and_block(self.window, "Maks. kwota", 10)
        total_pool_block = create_label_and_block(self.window, "Pula całkowita", 10)
        current_pool_block = create_label_and_block(self.window, "Aktualna pula", 10)
        branch_block = create_option_menu(self.window, "ID oddziału", "Wybierz", get_select("SELECT oddzial_id FROM oddzial_banku;"))
        # 

        # save btn
        save_button = tk.Button(self.window, text="Dodaj do bazy", command=save_name)
        save_button.pack(pady=10)
        # 

        # preview
        credit_preview = tk.Text(self.window, height=15, width=105)
        credit_preview.pack(pady=10)
        update_credit_preview()
        # 

        self.window.mainloop()

