from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculo de Salario Liquido")
        root.geometry("500x500+10+50") 
        
        self.label = Label(root, text="Calculadora de salario liquido").place(x=200, y=50)

        self.style = ttk.Style()
        
        entrada_salario = Entry(root, width=30)
        entrada_salario.place(x=150, y=100)
        

        self.button = Button(root, text="Inciar", command=self.on_button_click)
        self.button.pack(pady=10)

        self.tela()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def tela(self):
        self.root.configure(background='#00FF7F')


    def calcular_salario_liquido(self, entrada_salario):
        desconto_inss01 = 0.75

        if entrada_salario < 1612.00:
            desconto_inss01 = entrada_salario * desconto_inss01
        elif 1650.50 <= entrada_salario <= 2427.35:
            desconto_inss01 = entrada_salario * 0.09
        elif 2427.36 <= entrada_salario <= 3641.03:
            desconto_inss01 = entrada_salario * 0.12
        elif 3641.04 <= entrada_salario <= 7087.22:
            desconto_inss01 = entrada_salario * 0.14   

        return desconto_inss01
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()