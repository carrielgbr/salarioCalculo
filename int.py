from tkinter import *
from tkinter import ttk

## Calculo de salário 


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Salário")
        self.root.geometry("400x300")

        
        self.label = ttk.Label(root, text="Calculadora de Salário", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.salario = Entry(root, width=30, font=("Helvetica", 12))
        self.salario.pack(pady=10)
        self.salario.insert(0, "Digite seu salário")

        if  __name__ == '__main__':
            root = Tk()
            app = App(root)
            root.mainloop()