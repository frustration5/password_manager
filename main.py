import tkinter as tk
from tkinter import messagebox
import random
import json
import os


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()   # Main window
        self.window.title("Schloker Password Manager")
        # Canvas and settings to hold logo
        self.w_canvas = tk.Canvas(self.window, width=200, height=200, )
        self.main_img = tk.PhotoImage(file="./shlokerlogo.png")
        self.w_canvas.create_image(101, 99, image=self.main_img)
        self.w_canvas.grid(row=0, column=1, pady=(20, 2))
        # Buttons, save password entry and generate password
        self.save_b = tk.Button(self.window, text="Save Password Entry", font=("Consolas", 12, "bold"),
                                command=self.save_pw)
        self.save_b.grid(row=4, column=1, pady=(0, 10))
        self.gen_pw_b = tk.Button(self.window, text="Generate", font=("Consolas", 10, "bold"),
                                  command=self.populate_pw)
        self.gen_pw_b.grid(row=3, column=2, padx=(0, 15))
        # Various labels for the window
        self.url_l = tk.Label(self.window, text="URL: ", font=("Consolas", 12, "bold"))
        self.pw_l = tk.Label(self.window, text="Password: ", font=("Consolas", 12, "bold"))
        self.usr_l = tk.Label(self.window, text="Username: ", font=("Consolas", 12, "bold"))
        self.url_l.grid(row=1, column=0)
        self.usr_l.grid(row=2, column=0)
        self.pw_l.grid(row=3, column=0)
        self.url_e = tk.Entry(self.window, width=30, font="Consolas")
        self.pw_e = tk.Entry(self.window, width=20, font="Consolas")
        self.usr_e = tk.Entry(self.window, width=30, font="Consolas")
        # Entry widgets for entering info to save
        self.url_e.grid(row=1, column=1, columnspan=2, sticky="w")
        self.pw_e.grid(row=3, column=1, sticky="w")
        self.usr_e.grid(row=2, column=1, columnspan=2, sticky="w")
        self.password_length = 16
        # Defining the file path for keeping passwords and loading the contents for use
        self.pw_file = "./pws.json"
        self.pw_dict = self.load_password_from_file()

        self.window.mainloop()

    def generate_password(self):
        password_list = []
        a = "abcdefghijklmnopqrstuvwxyz"
        n = 1234567890
        for n in range(0, self.password_length + 1):
            if random.randint(0, 2) == 0:
                password_list.append(random.choice(a))
            elif random.randint(0, 2) == 1:
                password_list.append(random.choice(str(n)))
            else:
                password_list.append(random.choice(a.upper()))
        password = "".join(password_list)
        text_var = tk.StringVar()
        text_var.set(password)
        # print(password_list)
        return text_var

    def populate_pw(self):
        self.pw_e.config(textvariable=self.generate_password())

    def save_pw(self):
        url = self.url_e.get()
        usr = self.usr_e.get()
        pw = self.pw_e.get()
        if url == "" or pw == "" or usr == "":
            message = "One of the entries is empty, please fill in each field."
            tk.messagebox.showerror(title="Error", message=message)
        else:
            self.pw_dict[len(self.pw_dict)] = {"Username": usr, "URL": url, "Password": pw}
            self.write_password_to_file()

    def write_password_to_file(self):
        with open(self.pw_file, "w") as file:
            json.dump(self.pw_dict, file)

    def load_password_from_file(self):
        if os.path.exists(self.pw_file):
            with open(self.pw_file, "r") as file:
                try:
                    return json.load(file)
                except json.decoder.JSONDecodeError:
                    return {}
        else:
            message = "Password file is missing! Please create a .json file " \
                      "to store passwords " \
                      "at the applications root path."
            tk.messagebox.showerror(title="Error", message=message)
            self.window.destroy()


new_window = MainWindow()
