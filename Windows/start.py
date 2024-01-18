from Windows.common_tk_classes import *
from Windows.wi_clients import WindowInputClients
from Windows.wi_credit import WindowInputCredit
from Windows.wi_account import WindowInputAccount
from Windows.wi_branch import WindowInputBranch
from Windows.wi_card import WindowInputCard
from Windows.wi_credit_type import WindowInputCreditType
from Windows.wi_transfer import WindowInputTransfer
from Windows.wi_atm import WindowInputATM
from Windows.wi_transaction import WindowInputTransaction

class WindowStart(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)

    def win_ic_close(self, WindowClass, title):
        # self.window.destroy()
        windowInputClients = WindowClass(title)
        windowInputClients.vis()

    def vis(self):
        create_label_and_button(self.window, "Dodaj nowy oddział", "Nowy oddział", lambda: self.win_ic_close(WindowInputBranch, "Wprowadź nowy oddział"))
        create_label_and_button(self.window, "Dodaj nowego klienta", "Nowy klient", lambda: self.win_ic_close(WindowInputClients, "Wprowadź nowego klienta"))
        create_label_and_button(self.window, "Dodaj nowe konto", "Nowe konto", lambda: self.win_ic_close(WindowInputAccount, "Wprowadź nowe konto"))
        create_label_and_button(self.window, "Dodaj nową kartę", "Nowa karta", lambda: self.win_ic_close(WindowInputCard, "Wprowadź nową kartę"))
        create_label_and_button(self.window, "Dodaj nowy typ kredytu", "Nowy typ kredytu", lambda: self.win_ic_close(WindowInputCreditType, "Wprowadź nowy typ kredytu"))
        create_label_and_button(self.window, "Dodaj nowy kredyt", "Nowy kredyt", lambda: self.win_ic_close(WindowInputCredit, "Wprowadź nowy kredyt"))
        create_label_and_button(self.window, "Dodaj nowy przelew", "Nowy przelew", lambda: self.win_ic_close(WindowInputTransfer, "Wprowadź nowy przelew"))
        create_label_and_button(self.window, "Dodaj nowy bankomat", "Nowy bankomat", lambda: self.win_ic_close(WindowInputATM, "Wprowadź nowy bankomat"))
        create_label_and_button(self.window, "Dodaj nową transakcję", "Nowa transakcja", lambda: self.win_ic_close(WindowInputTransaction, "Wprowadź nową transakcję"))

        self.window.mainloop()

