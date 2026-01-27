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
        self.label.config(self.calcular_salario_liquido)

    def tela(self):
        self.root.configure(background='#00FF7F')


    def calcular_salario_liquido(self, entrada_salario):
        faixa1 = 1516.71 * 0.075 # 7.5%
        faixa2 = (2793.88 - 1516.71) * 0.09 # 9%
        faixa3 = (4190.83 - 2793.88) * 0.12 # 12%
        faixa4 = (8157.41 - 4190.83) * 0.14 # 14%
        teto = 8157.41 


        if entrada_salario < 1612.00:
            inss = entrada_salario * 0.075
        elif entrada_salario <= 2427.35:
            inss = (entrada_salario - 1516.71) * 0.09 + faixa1
        elif entrada_salario <= 4190.83:
            inss = (entrada_salario - 2793.88) * 0.12 + faixa1 + faixa2
        elif entrada_salario <= teto:
            inss = (entrada_salario - 4190.83) * 0.14 + faixa1 + faixa2 + faixa3
        else:
            inss = faixa1 + faixa2 + faixa3 + faixa4
        
        return round(inss, 2)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()