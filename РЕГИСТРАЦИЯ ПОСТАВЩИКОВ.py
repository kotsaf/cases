import tkinter as tk
from tkinter import Tk, RIGHT, BOTH, RAISED

All_objects = []

# основная логика
class Add_dealer(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Это всплывающее окно")
        self.btn_close_add_dealer = tk.Button(self, text="Закрыть", command=self.destroy)
        self.btn_add_dealer_name = tk.Button(
            self,
            text="Добавить",
            command=self.add_new_dealer                             # --- ()
        )
        self.txt_field_dealer_name = tk.Entry(self, width=10)


        self.txt_field_dealer_name.pack(padx=20, pady=20)
        self.label.pack(side=RIGHT, padx=20, pady=20)
        self.btn_add_dealer_name.pack(pady=5, ipadx=2, ipady=2)
        self.btn_close_add_dealer.pack(pady=5, ipadx=2, ipady=2)

    def add_new_dealer(self):                                       # --- , parent):
        self.new_dealer_name = self.txt_field_dealer_name.get()
        All_objects.append(self.new_dealer_name)
        print(All_objects)


# интерфейс
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn_open_add_dealer = tk.Button(self, text="Добавить поставщика",
                                             command=self.open_window_add_dealer)
        self.btn_open_add_dealer.pack(padx=50, pady=20)

    def open_window_add_dealer(self):
        window_add_dealer = Add_dealer(self)
        window_add_dealer.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
