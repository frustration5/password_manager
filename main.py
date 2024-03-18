import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import pyperclip


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()  # Main window
        self.window.title("Schloker Password Manager")
        self.window.config(width=800, height=800)
        # Canvas and settings to hold logo
        self.w_canvas = tk.Canvas(self.window, width=200, height=200)
        self.main_img = tk.PhotoImage(file="./shlokerlogo.png")
        self.w_canvas.create_image(99, 99, image=self.main_img)
        self.w_canvas.grid(row=0, column=1, pady=(20, 2))
        # Buttons, save password entry and generate password
        self.save_b = tk.Button(self.window, text="Save Password Entry", width=32, font=("Consolas", 12, "bold"),
                                command=self.save_pw)
        self.save_b.grid(row=4, column=1, columnspan=2, sticky="w", pady=(2, 2))
        self.gen_pw_b = tk.Button(self.window, text="Generate", font=("Consolas", 10, "bold"),
                                  command=self.populate_pw, width=12)
        self.gen_pw_b.grid(row=3, column=2, sticky="w", padx=(0, 10))
        self.copy_img = tk.PhotoImage(file="./copybutton.png").subsample(2, 2)
        self.copy_b = tk.Button(self.window, image=self.copy_img, command=self.copy)
        self.copy_b.grid(row=4, column=0)
        # Various labels for the window
        self.url_l = tk.Label(self.window, text="URL: ", font=("Consolas", 12, "bold"))
        self.pw_l = tk.Label(self.window, text="Password: ", font=("Consolas", 12, "bold"))
        self.usr_l = tk.Label(self.window, text="Username: ", font=("Consolas", 12, "bold"))
        self.url_l.grid(row=1, column=0, padx=(10, 0))
        self.usr_l.grid(row=2, column=0, padx=(10, 0))
        self.pw_l.grid(row=3, column=0, padx=(10, 0))
        self.url_e = tk.Entry(self.window, width=32, font="Consolas")
        self.url_e.focus()
        self.pw_e = tk.Entry(self.window, width=22, font="Consolas")
        self.usr_e = tk.Entry(self.window, width=32, font="Consolas")
        # Entry widgets for entering info to save
        self.url_e.grid(row=1, column=1, columnspan=2, sticky="w", padx=(0, 10))
        self.pw_e.grid(row=3, column=1, sticky="w")
        self.usr_e.grid(row=2, column=1, columnspan=2, sticky="w", padx=(0, 10))
        self.password_length = 16
        # Defining the file path for keeping passwords and loading the contents for use
        self.pw_file = "./pws.json"
        self.pw_dict = self.load_password_from_file()

        self.window.mainloop()

    def generate_password(self):
        password_list = []
        a = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ/*!%$&@#"
        for n in range(0, self.password_length + 1):
            password_list.append(random.choice(a))
        password = "".join(password_list)
        text_var = tk.StringVar()
        text_var.set(password)
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
            is_ok = messagebox.askokcancel(title="Confirm", message=f"Are you sure you want to save this entry?"
                                                                    f"\nURL: {url}\nUsername: {usr}\nPassword: {pw}\n")
            if is_ok:
                self.pw_dict[len(self.pw_dict)] = {"Username": usr, "URL": url, "Password": pw}
                self.write_password_to_file()
                self.url_e.delete(0, 'end')
                self.usr_e.delete(0, 'end')
                self.pw_e.delete(0, 'end')

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

    def copy(self):
        pyperclip.copy(self.pw_e.get())


new_window = MainWindow()
