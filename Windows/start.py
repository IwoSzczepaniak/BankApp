from Windows.common_tk_classes import *
from Windows.wi_clients import *
from Windows.wi_credit import *

class WindowStart(Window):
    def __init__(self, title) -> None:
        Window.__init__(self, title)

    def win_ic_close(self, WindowClass, title):
        self.window.destroy()
        windowInputClients = WindowClass(title)
        windowInputClients.vis()

    def vis(self):
        create_label_and_button(self.window, "Dodaj nowego klienta i zobacz ich podgląd", "Nowy klient", lambda: self.win_ic_close(WindowInputClients, "Wprowadź nowego klienta"))
        create_label_and_button(self.window, "Dodaj nowy kredyt", "Nowy kredyt", lambda: self.win_ic_close(WindowInputCredit, "Wprowadź nowy kredyt"))

        self.window.mainloop()

