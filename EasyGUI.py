import tkinter as tk
from tkinter import ttk

class EasyGUI:
    def __init__(self, title="EasyGUI", size="400x300"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.widgets = []
        
    def add_label(self, text, row, column, **kwargs):
        label = ttk.Label(self.root, text=text, **kwargs)
        label.grid(row=row, column=column, padx=5, pady=5)
        self.widgets.append(label)
        return label
        
    def add_button(self, text, command, row, column, **kwargs):
        button = ttk.Button(self.root, text=text, command=command, **kwargs)
        button.grid(row=row, column=column, padx=5, pady=5)
        self.widgets.append(button)
        return button
        
    def add_entry(self, row, column, **kwargs):
        entry = ttk.Entry(self.root, **kwargs)
        entry.grid(row=row, column=column, padx=5, pady=5)
        self.widgets.append(entry)
        return entry
        
    def add_checkbox(self, text, row, column, **kwargs):
        var = tk.IntVar()
        cb = ttk.Checkbutton(self.root, text=text, variable=var, **kwargs)
        cb.grid(row=row, column=column, padx=5, pady=5)
        self.widgets.append((cb, var))
        return cb, var
        
    def run(self):
        self.root.mainloop()


